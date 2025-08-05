#!/usr/bin/env python3
"""
Simple Instagram Card Image Generator using Playwright
"""

import os
import asyncio
from pathlib import Path

async def generate_image_playwright(html_file, output_file):
    """Generate PNG image from HTML using Playwright"""
    try:
        from playwright.async_api import async_playwright
        
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            
            # Set viewport to Instagram dimensions
            await page.set_viewport_size({"width": 1080, "height": 1080})
            
            # Load HTML file
            file_path = f"file://{os.path.abspath(html_file)}"
            await page.goto(file_path)
            
            # Wait for fonts and content to load
            await page.wait_for_timeout(3000)
            
            # Take screenshot
            await page.screenshot(path=output_file, full_page=False)
            
            await browser.close()
            print(f"✅ Generated: {output_file}")
            return True
            
    except ImportError:
        print("❌ Playwright not installed")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

async def main():
    """Generate all Instagram card images"""
    current_dir = Path(__file__).parent
    
    # Card files to process
    cards = [
        ('card-01-godard.html', 'godard-quote.png'),
        ('card-02-wenders.html', 'wenders-quote.png'),
        ('card-03-french.html', 'french-phrase.png'),
        ('card-04-dostoevsky.html', 'dostoevsky-quote.png'),
        ('card-05-philosophy.html', 'philosophy-quote.png'),
        ('card-06-heritage.html', 'heritage-quote.png'),
        ('card-07-elegance.html', 'elegance-quote.png'),
        ('card-08-vision.html', 'vision-quote.png'),
    ]
    
    print("🎨 Generating Instagram Cards (1080x1080 PNG)...\n")
    
    success_count = 0
    for html_file, png_file in cards:
        html_path = current_dir / html_file
        png_path = current_dir / png_file
        
        if html_path.exists():
            print(f"📱 Processing: {html_file}")
            if await generate_image_playwright(str(html_path), str(png_path)):
                success_count += 1
        else:
            print(f"❌ File not found: {html_file}")
    
    print(f"\n✨ Generated {success_count}/{len(cards)} images successfully!")

if __name__ == "__main__":
    asyncio.run(main())