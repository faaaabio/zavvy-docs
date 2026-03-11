"""
Captura screenshots do app Zavvy usando o perfil do Chrome (sessão já autenticada).
"""
import asyncio
import os
from playwright.async_api import async_playwright

CHROME_USER_DATA = r"C:\Users\fboo\AppData\Local\Google\Chrome\User Data"
OUTPUT_DIR = "screenshots/app"

PAGES = [
    # Dashboard
    {"path": "dashboard/01-home.png", "url": "https://app.zavvy.com.br/dashboard", "scroll": 0},
    {"path": "dashboard/02-home-bottom.png", "url": "https://app.zavvy.com.br/dashboard", "scroll": 9999},

    # Agenda
    {"path": "agenda/01-semana.png", "url": "https://app.zavvy.com.br/agenda", "scroll": 0},

    # Clientes - lista
    {"path": "clientes/01-lista.png", "url": "https://app.zavvy.com.br/clients", "scroll": 0},

    # Configurações
    {"path": "configuracoes/01-geral.png", "url": "https://app.zavvy.com.br/settings", "scroll": 0},
    {"path": "configuracoes/02-integracoes.png", "url": "https://app.zavvy.com.br/settings", "scroll": 9999},
]

MODAL_PAGES = [
    # Agenda com modal aberto - feito separado via js
]


async def capture(page, config):
    out = os.path.join(OUTPUT_DIR, config["path"])
    os.makedirs(os.path.dirname(out), exist_ok=True)

    if page.url != config["url"]:
        await page.goto(config["url"], wait_until="networkidle")
        await page.wait_for_timeout(1500)

    if config.get("scroll", 0) == 0:
        await page.evaluate("window.scrollTo(0, 0)")
    else:
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    await page.wait_for_timeout(600)
    await page.screenshot(path=out)
    print(f"  Saved: {out}")


async def main():
    async with async_playwright() as p:
        # Usa contexto persistente com o perfil do Chrome
        context = await p.chromium.launch_persistent_context(
            user_data_dir=CHROME_USER_DATA,
            headless=True,
            channel="chrome",
            viewport={"width": 1280, "height": 860},
            args=["--disable-blink-features=AutomationControlled"],
        )

        page = context.pages[0] if context.pages else await context.new_page()

        # Testa autenticação
        await page.goto("https://app.zavvy.com.br/dashboard", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        print(f"URL atual: {page.url}")

        if "login" in page.url:
            print("⚠️  Não autenticado no perfil headless. Tentando via Chrome visível...")
            await context.close()
            context = await p.chromium.launch_persistent_context(
                user_data_dir=CHROME_USER_DATA,
                headless=False,
                channel="chrome",
                viewport={"width": 1280, "height": 860},
            )
            page = context.pages[0] if context.pages else await context.new_page()
            await page.goto("https://app.zavvy.com.br/dashboard", wait_until="networkidle")
            await page.wait_for_timeout(2000)
            print(f"URL atual: {page.url}")

        if "login" in page.url:
            print("❌ Sessão não disponível. Abortando.")
            await context.close()
            return

        print("✅ Autenticado. Capturando screenshots...\n")

        for config in PAGES:
            print(f"[{config['path']}]")
            await capture(page, config)

        # Cliente detalhe - pegar o primeiro cliente
        await page.goto("https://app.zavvy.com.br/clients", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # Clica no primeiro cliente da lista
        client_row = page.locator("table tr, [role='row']").nth(1)
        if await client_row.count() > 0:
            await client_row.click()
            await page.wait_for_timeout(1000)
            out = os.path.join(OUTPUT_DIR, "clientes/02-perfil-historico.png")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            await page.screenshot(path=out)
            print(f"  Saved: {out}")

            # Aba Anotações
            try:
                await page.click("text=Anotações")
                await page.wait_for_timeout(600)
                out = os.path.join(OUTPUT_DIR, "clientes/03-perfil-anotacoes.png")
                await page.screenshot(path=out)
                print(f"  Saved: {out}")
            except Exception as e:
                print(f"  Skip Anotações: {e}")

        # Agenda com modal
        await page.goto("https://app.zavvy.com.br/agenda", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        out = os.path.join(OUTPUT_DIR, "agenda/01-semana.png")
        await page.screenshot(path=out)
        print(f"  Saved: {out}")

        # Tenta abrir um agendamento
        try:
            event = page.locator(".fc-event, [class*='event'], [class*='appointment']").first
            if await event.count() > 0:
                await event.click()
                await page.wait_for_timeout(800)
                out = os.path.join(OUTPUT_DIR, "agenda/02-modal-detalhe.png")
                await page.screenshot(path=out)
                print(f"  Saved: {out}")
        except Exception as e:
            print(f"  Skip modal: {e}")

        await context.close()
        print("\n✅ Captura concluída!")


if __name__ == "__main__":
    asyncio.run(main())
