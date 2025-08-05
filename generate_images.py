#!/usr/bin/env python3
"""
Instagram Card Image Generator
Converts HTML cards to 1080x1080 PNG images for Instagram posts
"""

import os
import time
import subprocess
from pathlib import Path

def generate_image_with_wkhtmltoimage(html_file, output_file):
    """
    Generate PNG image from HTML using wkhtmltoimage
    """
    try:
        cmd = [
            'wkhtmltoimage',
            '--width', '1080',
            '--height', '1080',
            '--format', 'png',
            '--quality', '100',
            '--javascript-delay', '1000',
            '--no-stop-slow-scripts',
            '--load-media-error-handling', 'ignore',
            html_file,
            output_file
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Generated: {output_file}")
            return True
        else:
            print(f"❌ Error generating {output_file}: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ wkhtmltoimage not found. Please install it:")
        print("   Ubuntu/Debian: sudo apt-get install wkhtmltopdf")
        print("   macOS: brew install wkhtmltopdf")
        print("   Or use alternative method with playwright/selenium")
        return False

def generate_image_with_playwright(html_file, output_file):
    """
    Alternative method using Playwright (requires: pip install playwright)
    """
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Set viewport to Instagram dimensions
            page.set_viewport_size({"width": 1080, "height": 1080})
            
            # Load HTML file
            page.goto(f"file://{os.path.abspath(html_file)}")
            
            # Wait for fonts and content to load
            page.wait_for_timeout(2000)
            
            # Take screenshot
            page.screenshot(path=output_file, full_page=True)
            
            browser.close()
            print(f"✅ Generated: {output_file}")
            return True
            
    except ImportError:
        print("❌ Playwright not found. Install with: pip install playwright")
        print("   Then run: playwright install chromium")
        return False
    except Exception as e:
        print(f"❌ Error generating {output_file}: {str(e)}")
        return False

def generate_all_images():
    """
    Generate PNG images for all HTML card files
    """
    current_dir = Path(__file__).parent
    
    # Card files to process
    card_files = [
        ('card-01-godard.html', 'godard-quote.png'),
        ('card-02-wenders.html', 'wenders-quote.png'),
        ('card-03-french.html', 'french-phrase.png'),
        ('card-04-dostoevsky.html', 'dostoevsky-quote.png'),
    ]
    
    print("🎨 Generating Instagram Cards (1080x1080 PNG)...\n")
    
    success_count = 0
    
    for html_file, png_file in card_files:
        html_path = current_dir / html_file
        png_path = current_dir / png_file
        
        if not html_path.exists():
            print(f"❌ HTML file not found: {html_path}")
            continue
        
        print(f"📱 Processing: {html_file} → {png_file}")
        
        # Try wkhtmltoimage first, then fallback to playwright
        success = generate_image_with_wkhtmltoimage(str(html_path), str(png_path))
        
        if not success:
            print("   Trying alternative method...")
            success = generate_image_with_playwright(str(html_path), str(png_path))
        
        if success:
            success_count += 1
        
        print()
    
    print(f"✨ Generated {success_count}/{len(card_files)} images successfully!")
    
    if success_count > 0:
        print("\n📋 Instructions for remaining cards:")
        print("1. Open the HTML files in a browser")
        print("2. Set browser window to 1080x1080 pixels")
        print("3. Use browser developer tools to take screenshot")
        print("4. Or use online HTML-to-image converters")

def create_additional_cards():
    """
    Create remaining card HTML files
    """
    current_dir = Path(__file__).parent
    
    # Additional cards content
    additional_cards = [
        {
            'filename': 'card-05-philosophy.html',
            'title': 'Art Philosophy - Instagram Card',
            'background': 'linear-gradient(135deg, #4a4a4a 0%, #2c1810 50%, #8b4513 100%)',
            'color': '#f5f5f5',
            'content': '''
            <div class="quote-text">Drawing inspiration from the great masters of photography</div>
            <div class="artistic-accent">Edward Weston • Helmut Newton • Man Ray</div>
            <div class="english-translation">Classical composition meets contemporary minimalism</div>
            ''',
            'tag': 'Philosophy',
            'decorative': '🎭'
        },
        {
            'filename': 'card-06-heritage.html',
            'title': 'Photography Heritage - Instagram Card',
            'background': 'linear-gradient(135deg, #1a1a1a 0%, #3c3c3c 50%, #d4af37 100%)',
            'color': '#ffffff',
            'content': '''
            <div class="quote-text">Photography is not just documentation, but poetry made visible</div>
            <div class="artistic-accent">Julia Margaret Cameron • Man Ray</div>
            <div class="english-translation">Rooted in fine art tradition</div>
            ''',
            'tag': 'Heritage',
            'decorative': '🏛️'
        },
        {
            'filename': 'card-07-elegance.html',
            'title': 'European Elegance - Instagram Card',
            'background': 'linear-gradient(135deg, #5c4033 0%, #8b6914 50%, #2c1810 100%)',
            'color': '#f5f5f5',
            'content': '''
            <div class="quote-text">Sophisticated European art cinema aesthetics</div>
            <div class="french-text">Élégance intemporelle</div>
            <div class="english-translation">Timeless elegance in every frame</div>
            ''',
            'tag': 'Elegance',
            'decorative': '👑'
        },
        {
            'filename': 'card-08-vision.html',
            'title': 'Artistic Vision - Instagram Card',
            'background': 'linear-gradient(135deg, #2c2c54 0%, #40407a 50%, #706fd3 100%)',
            'color': '#ffffff',
            'content': '''
            <div class="quote-text">Creating images that are both timeless and thoroughly modern</div>
            <div class="artistic-accent">Richard Avedon • Annie Leibovitz</div>
            <div class="english-translation">Narrative storytelling through lens</div>
            ''',
            'tag': 'Vision',
            'decorative': '🌟'
        }
    ]
    
    # Base HTML template
    html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1080, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300;400;600;700&family=Lato:wght@300;400;600&family=Dancing+Script:wght@400;600;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400;1,600&display=swap" rel="stylesheet">
    <style>
        body {{ margin: 0; padding: 0; width: 1080px; height: 1080px; overflow: hidden; }}
        .instagram-card {{
            width: 1080px; height: 1080px; position: relative; overflow: hidden;
            background: {background}; color: {color}; 
            display: flex; align-items: center; justify-content: center;
        }}
        .card-content {{ padding: 80px; text-align: center; position: relative; z-index: 2; }}
        .quote-text {{ font-family: 'Playfair Display', serif; font-size: 36px; font-weight: 400; 
            line-height: 1.4; margin-bottom: 40px; font-style: italic; position: relative; }}
        .french-text {{ font-family: 'Dancing Script', cursive; font-size: 48px; font-weight: 600; 
            color: #d4af37; margin: 30px 0; text-align: center; }}
        .english-translation {{ font-family: 'Cormorant Garamond', serif; font-size: 24px; 
            font-style: italic; opacity: 0.9; margin-bottom: 30px; }}
        .artistic-accent {{ font-family: 'Cormorant Garamond', serif; font-size: 20px; 
            font-style: italic; opacity: 0.8; margin-top: 20px; }}
        .brand-footer {{ position: absolute; bottom: 40px; left: 80px; right: 80px; 
            display: flex; justify-content: space-between; align-items: center; 
            border-top: 2px solid rgba(255, 255, 255, 0.2); padding-top: 20px; }}
        .brand-name {{ font-family: 'Playfair Display', serif; font-size: 28px; 
            font-weight: 600; letter-spacing: 3px; }}
        .instagram-handle {{ font-family: 'Lato', sans-serif; font-size: 18px; opacity: 0.9; }}
        .specialty-tag {{ position: absolute; top: 40px; right: 40px; 
            background: rgba(212, 175, 55, 0.9); color: #000; padding: 15px 30px; 
            border-radius: 25px; font-size: 14px; font-weight: 600; text-transform: uppercase; }}
        .decorative-element {{ position: absolute; top: 50%; left: 50%; 
            transform: translate(-50%, -50%); opacity: 0.05; font-size: 250px; z-index: 1; }}
    </style>
</head>
<body>
    <div class="instagram-card">
        <div class="decorative-element">{decorative}</div>
        <div class="specialty-tag">{tag}</div>
        <div class="card-content">
            {content}
        </div>
        <div class="brand-footer">
            <div class="brand-name">ARTY</div>
            <div class="instagram-handle">@Krish_Payn</div>
        </div>
    </div>
</body>
</html>'''
    
    # Create additional card files
    for card in additional_cards:
        filepath = current_dir / card['filename']
        html_content = html_template.format(**card)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"📝 Created: {card['filename']}")

if __name__ == "__main__":
    print("🎨 Instagram Card Generator for ARTY Photography\n")
    
    # Create additional card files
    print("📝 Creating additional card HTML files...")
    create_additional_cards()
    
    print("\n" + "="*50)
    
    # Generate images
    generate_all_images()
    
    print("\n🎯 All cards are ready for Instagram!")
    print("📱 Each card is designed at 1080x1080 pixels for optimal Instagram posting")