# EmailJS Setup Guide - ARTY Photography Contact Form

## 🚀 **Quick Setup (5 minutes)**

Your contact form is now ready to send real emails! Follow these steps to activate it:

---

## **Step 1: Create EmailJS Account**

1. **Go to**: [https://www.emailjs.com](https://www.emailjs.com)
2. **Sign up** for a free account (100 emails/month free)
3. **Confirm** your email address

---

## **Step 2: Create Email Service**

1. **Go to** Email Services in your EmailJS dashboard
2. **Click** "Add New Service"
3. **Choose** your email provider:
   - **Gmail** (recommended for srivonx@gmail.com)
   - **Outlook**
   - **Yahoo**
   - **Or any SMTP service**

4. **Connect** your Gmail account (`srivonx@gmail.com`)
5. **Copy** the Service ID (looks like: `service_xxxxxxx`)

---

## **Step 3: Create Email Template**

1. **Go to** Email Templates in your dashboard
2. **Click** "Create New Template"
3. **Use this template**:

```
Subject: New Photography Inquiry - {{service_type}}

From: {{from_name}}
Email: {{from_email}}
Service: {{service_type}}

Message:
{{message}}

---
Sent from ARTY Photography website
Contact: srivonx@gmail.com
Instagram: @Krish_Payn
```

4. **Save** and copy the Template ID (looks like: `template_xxxxxxx`)

---

## **Step 4: Get Public Key**

1. **Go to** Account → API Keys
2. **Copy** your Public Key (looks like: `your_public_key_here`)

---

## **Step 5: Update Website Code**

**Edit `script.js` and replace these 3 values:**

```javascript
// Line 80: Replace YOUR_PUBLIC_KEY
emailjs.init("your_actual_public_key_here");

// Line 127: Replace YOUR_SERVICE_ID and YOUR_TEMPLATE_ID
emailjs.send('your_service_id_here', 'your_template_id_here', templateParams)
```

**Example:**
```javascript
emailjs.init("user_abc123def456");
emailjs.send('service_gmail123', 'template_contact456', templateParams)
```

---

## **Step 6: Test the Form**

1. **Open** your website
2. **Fill out** the contact form
3. **Submit** and check `srivonx@gmail.com` for the email
4. **Success!** ✅

---

## **📧 Email Template Variables**

Your form sends these variables to EmailJS:

- `{{from_name}}` - Customer's name
- `{{from_email}}` - Customer's email  
- `{{service_type}}` - Selected photography service
- `{{message}}` - Customer's message
- `{{to_email}}` - Your email (srivonx@gmail.com)

---

## **🎨 Form Features**

**Enhanced UX:**
- ✅ **Real email sending** to srivonx@gmail.com
- ✅ **Form validation** with visual feedback
- ✅ **Loading states** - "Sending..." → "Message Sent!"
- ✅ **Error handling** - "Error - Try Again"
- ✅ **Auto-reset** form after successful submission
- ✅ **Professional styling** matches website design

**Visual Feedback:**
- 🟢 **Green button** on success
- 🔴 **Red button** on error  
- 🟡 **Golden button** while sending
- 🔴 **Red borders** for validation errors
- 🟡 **Golden borders** for valid fields

---

## **📱 Mobile & Desktop Ready**

- **Responsive design** works on all devices
- **Touch-friendly** form elements
- **Professional appearance** maintains brand consistency
- **Fast loading** with CDN integration

---

## **🔒 Security & Privacy**

- **No backend required** - secure client-side processing
- **EmailJS handles** all email delivery securely
- **Form data** never stored on your website
- **GDPR compliant** email service

---

## **💡 Customization Options**

**Email Templates:** Customize the email format in EmailJS dashboard
**Validation:** Add more fields or validation rules in script.js
**Styling:** Modify form appearance in styles.css
**Recipients:** Add multiple recipients in EmailJS settings

---

## **🎯 Free Tier Limits**

- **100 emails/month** free
- **Upgrade** to paid plans for more volume
- **Perfect** for photography business contact forms

---

## **✨ Your Form Will:**

1. **Validate** all required fields
2. **Send** professional emails to srivonx@gmail.com
3. **Show** elegant loading and success states
4. **Maintain** your sophisticated brand aesthetic
5. **Work** perfectly on all devices

**Setup takes 5 minutes and your contact form will be fully functional! 🚀**

---

## **🆘 Troubleshooting**

**Form not sending?**
- Check all 3 IDs are correctly replaced in script.js
- Verify EmailJS service is connected to srivonx@gmail.com
- Check browser console for error messages

**Need help?** The EmailJS dashboard has excellent documentation and support.

**Your elegant, functional contact form is ready to capture photography inquiries! 📸✨**