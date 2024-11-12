from behave import given, when, then
from playwright.sync_api import sync_playwright
import time
import asyncio


@given('the user is at the challenge page')
async def step_impl(context):
    async with async_playwright() as playwright:
    # Launch Playwright browser and open the login page
        context.browser = sync_playwright().start().chromium.launch(headless=False)
        context.page = context.browser.new_page()
        page.start_tracing(path="trace.zip")
        context.page.goto('https://b_co2efane4o4.v0.build/')
        context.page.wait_for_load_state("load")
        assert context.page.url == "https://b_co2efane4o4.v0.build/"
        time.sleep(2)

@when('the user click zap the answer')
@when('the user click zap the answer')
async def step_impl(context):
    #context.page.locator("iframe").content_frame.get_by_role("button", name="Zap Your Answers!").click()
    context.page.locator("iframe").content_frame.locator("//button[contains(text(), 'Zap Your Answers!')]").wait_for(state="visible")
    time.sleep(2)
    context.page.locator("iframe").content_frame.locator("//button[contains(text(), 'Zap Your Answers!')]").click()


@then('the user is shown zap successfully message')
async def step_impl(context):
    context.page.locator("iframe").content_frame.locator("//h2[contains(text(), 'Congratulations')]").click()

@when('the user type "{text}"')
async def step_impl(context, text):
   context.page.locator("iframe").content_frame.locator("//input[contains(@placeholder, 'E.g., Invisibility')]").fill(text)





