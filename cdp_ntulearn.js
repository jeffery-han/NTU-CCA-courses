const httpBase = 'http://127.0.0.1:9222';

async function listPages() {
  return (await fetch(`${httpBase}/json/list`)).json();
}

async function evaluate(page, expression) {
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    ws.onopen = resolve;
    ws.onerror = reject;
  });
  return new Promise((resolve, reject) => {
    const id = 1;
    ws.onmessage = event => {
      const message = JSON.parse(event.data);
      if (message.id !== id) return;
      ws.close();
      if (message.error) reject(new Error(JSON.stringify(message.error)));
      else resolve(message.result?.result?.value);
    };
    ws.send(JSON.stringify({
      id,
      method: 'Runtime.evaluate',
      params: { expression, returnByValue: true, awaitPromise: true }
    }));
  });
}

async function command(page, method, params = {}) {
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    ws.onopen = resolve;
    ws.onerror = reject;
  });
  return new Promise((resolve, reject) => {
    const id = 1;
    ws.onmessage = event => {
      const message = JSON.parse(event.data);
      if (message.id !== id) return;
      ws.close();
      if (message.error) reject(new Error(JSON.stringify(message.error)));
      else resolve(message.result);
    };
    ws.send(JSON.stringify({ id, method, params }));
  });
}

async function main() {
  const pages = (await listPages()).filter(p => p.type === 'page' && p.url.startsWith('http'));
  if (process.argv[2] === 'navigate') {
    const page = pages[0];
    await command(page, 'Page.navigate', { url: process.argv[3] });
    console.log('NAVIGATED');
    return;
  }
  if (process.argv[2] === 'click') {
    const page = pages[0];
    const selector = process.argv[3];
    const result = await evaluate(page, `(() => {
      const element = document.querySelector(${JSON.stringify(selector)});
      if (!element) return 'NOT_FOUND';
      element.click();
      return 'CLICKED';
    })()`);
    console.log(result);
    return;
  }
  if (process.argv[2] === 'find-text') {
    const page = pages[0];
    const needle = process.argv[3];
    const result = await evaluate(page, `(() => {
      const needle = ${JSON.stringify(needle)};
      const matches = [...document.querySelectorAll('*')].filter(e =>
        e.children.length === 0 && (e.textContent || '').includes(needle)
      );
      return matches.slice(0, 10).map(e => e.parentElement?.parentElement?.outerHTML?.slice(0, 6000));
    })()`);
    console.log(JSON.stringify(result));
    return;
  }
  if (process.argv[2] === 'enter-email') {
    const email = process.argv[3];
    let page;
    for (const candidate of pages) {
      if (await evaluate(candidate, `Boolean(document.querySelector('input[type="email"]'))`)) {
        page = candidate;
        break;
      }
    }
    if (!page) throw new Error('EMAIL_INPUT_NOT_FOUND');
    await command(page, 'Page.bringToFront');
    await evaluate(page, `(() => { const i = document.querySelector('input[type="email"]'); i.focus(); i.select(); return true; })()`);
    await command(page, 'Input.insertText', { text: email });
    const point = await evaluate(page, `(() => {
      const b = document.querySelector('#idSIButton9');
      b.scrollIntoView({ block: 'center' });
      const r = b.getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    })()`);
    await command(page, 'Input.dispatchMouseEvent', { type: 'mousePressed', x: point.x, y: point.y, button: 'left', clickCount: 1 });
    await command(page, 'Input.dispatchMouseEvent', { type: 'mouseReleased', x: point.x, y: point.y, button: 'left', clickCount: 1 });
    await evaluate(page, `(() => { document.querySelector('#idSIButton9').click(); return true; })()`);
    console.log('EMAIL_SUBMITTED');
    return;
  }
  for (const page of pages) {
    const info = await evaluate(page, `JSON.stringify({
      title: document.title,
      url: location.href,
      text: document.body?.innerText?.slice(0, 1600),
      inputs: [...document.querySelectorAll('input')].map(i => ({
        id: i.id, type: i.type, name: i.name, placeholder: i.placeholder,
        autocomplete: i.autocomplete, hasValue: Boolean(i.value), disabled: i.disabled,
        rect: (() => { const r=i.getBoundingClientRect(); return {x:r.x,y:r.y,w:r.width,h:r.height}; })()
      })),
      buttons: [...document.querySelectorAll('button,input[type="submit"]')].map(b => ({
        id: b.id, type: b.type, text: b.innerText || b.value, disabled: b.disabled
      })),
      links: [...document.querySelectorAll('a[href]')].slice(0, 100).map(a => ({
        text: (a.innerText || a.getAttribute('aria-label') || '').trim(), href: a.href
      })),
      forms: [...document.forms].map(f => ({ id: f.id, action: f.action, method: f.method }))
    })`);
    console.log(info);
  }
}

main().catch(error => {
  console.error(error);
  process.exitCode = 1;
});
