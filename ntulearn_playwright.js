const { chromium } = require('C:/Users/26371/AppData/Local/Temp/CodexNTUAutomation/node_modules/playwright-core');

async function pageState(page) {
  return {
    title: await page.title(),
    url: page.url(),
    text: (await page.locator('body').innerText().catch(() => '')).slice(0, 1200)
  };
}

async function main() {
  const email = process.argv[2];
  const password = process.argv[3];
  const browser = await chromium.connectOverCDP('http://127.0.0.1:9222');
  const context = browser.contexts()[0];
  let page = context.pages().find(p => p.url().startsWith('http'));
  if (!page) page = await context.newPage();
  await page.bringToFront();

  if (!page.url().includes('login.microsoftonline.com')) {
    await page.goto('https://ntulearn.ntu.edu.sg', { waitUntil: 'domcontentloaded' });
  }

  const emailInput = page.locator('input[type="email"]');
  if (await emailInput.isVisible().catch(() => false)) {
    await emailInput.fill(email);
    await page.locator('#idSIButton9').click();
    await page.waitForTimeout(2500);
  }

  const passwordInput = page.locator('input[type="password"]');
  if (password && await passwordInput.isVisible().catch(() => false)) {
    await passwordInput.fill(password);
    await page.locator('#idSIButton9').click();
    await page.waitForTimeout(3500);
  }

  if (await page.locator('#KmsiCheckboxField').isVisible().catch(() => false)) {
    await page.locator('#idSIButton9').click({ noWaitAfter: true });
    await page.waitForTimeout(5000);
  }

  console.log(JSON.stringify(await pageState(page)));
  process.exit(0);
}

main().catch(error => {
  console.error(error.message);
  process.exitCode = 1;
});
