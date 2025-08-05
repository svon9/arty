#!/usr/bin/env python3
"""
Minimalist ARTY Logo Generator - Website Color Scheme
Uses grey (#333), black, and golden (#d4af37) colors from index.html
"""

import os
import asyncio
from pathlib import Path

async def generate_minimalist_logo(html_file, output_file):
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
    """Generate all minimalist ARTY logo variations"""
    current_dir = Path(__file__).parent
    
    # Minimalist logo files to process
    logos = [
        ('minimalist-logo-01.html', 'arty-minimal-clean.png'),
        ('minimalist-logo-02.html', 'arty-minimal-circle.png'),
        ('minimalist-logo-03.html', 'arty-minimal-negative.png'),
        ('minimalist-logo-04.html', 'arty-minimal-abstract.png'),
        ('minimalist-logo-05.html', 'arty-minimal-letter-a.png'),
        ('minimalist-logo-06.html', 'arty-minimal-grid.png'),
    ]
    
    print("🎨 Generating Minimalist ARTY Logo Collection...\n")
    print("🎯 Using Website Color Scheme: Grey (#333), Black, Gold (#d4af37)")
    print("📱 500x500px - Perfect for Instagram Profile\n")
    
    success_count = 0
    for html_file, png_file in logos:
        html_path = current_dir / html_file
        png_path = current_dir / png_file
        
        if html_path.exists():
            print(f"🎭 Processing: {html_file}")
            if await generate_minimalist_logo(str(html_path), str(png_path)):
                success_count += 1
        else:
            print(f"❌ File not found: {html_file}")
    
    print(f"\n✨ Generated {success_count}/{len(logos)} minimalist logos successfully!")
    
    if success_count > 0:
        print("\n🎨 Minimalist Logo Collection Features:")
        print("• Clean Typography - lowercase 'arty' text")
        print("• Artistic Minimalism - geometric shapes and lines")
        print("• Website Color Harmony - matches index.html perfectly")
        print("• Professional Aesthetic - sophisticated and clean")
        print("• Instagram Ready - 500x500px optimal dimensions")
        
        print("\n🌟 Logo Variations:")
        print("1. Clean Typography - geometric frame with dots")
        print("2. Circle Frame - enclosed brand name with accents")
        print("3. Negative Space - dark background with light text")
        print("4. Abstract Symbol - overlapping circles with line")
        print("5. Letter A Artistic - large 'a' with golden line")
        print("6. Grid System - pixel art style 'A' pattern")

if __name__ == "__main__":
    asyncio.run(main())