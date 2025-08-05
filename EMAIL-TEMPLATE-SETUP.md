# EmailJS Template Setup Guide

## 📧 **Step-by-Step Email Template Creation**

After creating your EmailJS account and service, here's exactly how to create the email template:

---

## **Step 1: Access Email Templates**

1. **Login** to your EmailJS dashboard at [emailjs.com](https://www.emailjs.com)
2. **Click** on "Email Templates" in the left sidebar
3. **Click** the "Create New Template" button

---

## **Step 2: Template Settings**

**Template Name:** `ARTY Photography Contact Form`

**Template ID:** (will be auto-generated, looks like `template_xxxxxxx`)

---

## **Step 3: Email Template Content**

### **Subject Line:**
```
New Photography Inquiry - {{service_type}} | ARTY
```

### **Email Body (Copy this exactly):**
```
🎨 NEW PHOTOGRAPHY INQUIRY - ARTY FINE ART & BOUDOIR

📞 CONTACT DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name: {{from_name}}
Email: {{from_email}}
Service Interest: {{service_type}}

💬 CLIENT MESSAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{{message}}

🎭 PHOTOGRAPHY SERVICES PRICING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Classic Boudoir: ₹15,000 - ₹25,000
• Luxury Fashion: ₹40,000 - ₹65,000  
• Fine Art Form: ₹35,000 - ₹55,000
• Elite Experience: ₹80,000 - ₹100,000
• Couples Intimacy: ₹30,000 - ₹45,000
• Maternity Art: ₹20,000 - ₹35,000

📱 QUICK RESPONSE TEMPLATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hello {{from_name}},

Thank you for your interest in {{service_type}} photography session. I'd love to discuss your vision and create something beautiful together.

Let's schedule a consultation to discuss:
• Your photography goals and style preferences
• Session details and location options
• Investment and package options
• Available dates

Best regards,
ARTY Photography
Email: srivonx@gmail.com
Instagram: @Krish_Payn

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎨 ARTY - Fine Art & Boudoir Photography
L'art de capturer l'âme
Website: [Your Website URL]
Location: Bhubaneswar & Premium Venues
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This email was sent from ARTY Photography contact form.
```

---

## **Step 4: Template Variables**

**Make sure these variables are exactly as shown:**

- `{{from_name}}` - Customer's name
- `{{from_email}}` - Customer's email address  
- `{{service_type}}` - Selected photography service
- `{{message}}` - Customer's personal message

**(These must match the JavaScript code exactly!)**

---

## **Step 5: Email Settings**

### **From Name:** 
```
ARTY Photography Contact Form
```

### **From Email:** 
```
noreply@emailjs.com
```
*(EmailJS will handle this automatically)*

### **Reply To:**
```
{{from_email}}
```
*(This allows you to reply directly to the customer)*

### **To Email:**
```
srivonx@gmail.com
```

---

## **Step 6: Test Your Template**

1. **Click** "Test Template" button in EmailJS
2. **Fill in** sample data:
   ```
   from_name: John Smith
   from_email: john@example.com
   service_type: Classic Boudoir
   message: I'm interested in a boudoir session for my wife's birthday
   ```
3. **Send test** email to srivonx@gmail.com
4. **Check** your inbox for the formatted email

---

## **Step 7: Save and Copy Template ID**

1. **Click** "Save" button
2. **Copy** the Template ID (example: `template_abc123def`)
3. **Use this ID** in your website's script.js file

---

## **📱 What Your Email Will Look Like:**

```
Subject: New Photography Inquiry - Classic Boudoir | ARTY

🎨 NEW PHOTOGRAPHY INQUIRY - ARTY FINE ART & BOUDOIR

📞 CONTACT DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name: Sarah Johnson
Email: sarah@example.com
Service Interest: Classic Boudoir

💬 CLIENT MESSAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Hi! I'm interested in booking a boudoir session as a gift for my husband. I'd love to discuss the classic boudoir package and available dates in Bhubaneswar.

[Rest of template with pricing and contact info...]
```

---

## **🎨 Template Features:**

✅ **Professional formatting** with emojis and dividers
✅ **All service pricing** included for quick reference  
✅ **Customer details** clearly displayed
✅ **Response template** ready to copy-paste
✅ **Brand consistency** with ARTY aesthetic
✅ **Contact information** prominently displayed
✅ **Instagram handle** for social media connection

---

## **🔧 After Creating Template:**

1. **Copy the Template ID** (looks like: `template_xxxxxxx`)
2. **Go to your website's script.js file**
3. **Replace** `YOUR_TEMPLATE_ID` with your actual Template ID:

```javascript
// Before:
emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', templateParams)

// After:
emailjs.send('service_gmail123', 'template_abc123def', templateParams)
```

---

## **✨ Your Email Template Will:**

- 📧 Send beautifully formatted emails to srivonx@gmail.com
- 🎨 Include all customer details and service selection
- 💼 Display professional ARTY branding
- 📱 Show all photography packages and pricing
- 🔄 Allow direct reply to customer
- ⚡ Work instantly with your contact form

**Your professional email template is ready to impress potential clients! 🎭✨**