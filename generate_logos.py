#!/usr/bin/env python3
"""
ARTY Logo Generator - Creates Instagram-ready logo files
"""

import os
import asyncio
from pathlib import Path

async def generate_logo_image(html_file, output_file):
    """Generate PNG logo from HTML using Playwright"""
    try:
        from playwright.async_api import async_playwright
        
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            
            # Set viewport for Instagram profile dimensions (500x500)
            await page.set_viewport_size({"width": 500, "height": 500})
            
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
            
    except Exception as e:
        print(f"❌ Error generating {output_file}: {str(e)}")
        return False

async def main():
    """Generate all ARTY logo variations"""
    current_dir = Path(__file__).parent
    
    # Logo files to process
    logos = [
        ('logo-01-minimalist.html', 'arty-logo-minimalist.png'),
        ('logo-02-cinematic.html', 'arty-logo-cinematic.png'),
        ('logo-03-french-elegance.html', 'arty-logo-french.png'),
        ('logo-04-geometric-modern.html', 'arty-logo-geometric.png'),
        ('logo-05-vintage-luxe.html', 'arty-logo-vintage.png'),
        ('logo-06-monogram.html', 'arty-logo-monogram.png'),
    ]
    
    print("🎨 Generating ARTY Logo Collection (500x500 PNG)...\n")
    print("🎯 Perfect for Instagram Profile Pictures & Branding\n")
    
    success_count = 0
    for html_file, png_file in logos:
        html_path = current_dir / html_file
        png_path = current_dir / png_file
        
        if html_path.exists():
            print(f"🎭 Processing: {html_file}")
            if await generate_logo_image(str(html_path), str(png_path)):
                success_count += 1
        else:
            print(f"❌ File not found: {html_file}")
    
    print(f"\n✨ Generated {success_count}/{len(logos)} logos successfully!")
    
    if success_count > 0:
        print("\n🎨 Logo Collection Complete!")
        print("📱 All logos are 500x500px - perfect for Instagram profile")
        print("🎯 Each logo reflects sophisticated European aesthetics")
        print("🌟 Choose your favorite for @Krish_Payn branding!")

if __name__ == "__main__":
    asyncio.run(main())