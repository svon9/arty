// Smooth scrolling navigation
document.addEventListener('DOMContentLoaded', function() {
    // Navigation links smooth scrolling
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Get target section
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                // Smooth scroll to target
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Update active navigation on scroll
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('section');
        const scrollPos = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            const correspondingLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);

            if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                navLinks.forEach(link => link.classList.remove('active'));
                if (correspondingLink) {
                    correspondingLink.classList.add('active');
                }
            }
        });
    });

    // Service card hover animations
    const serviceCards = document.querySelectorAll('.service-card');
    
    serviceCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Location card animations
    const locationCards = document.querySelectorAll('.location-card');
    
    locationCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 10px 25px rgba(0, 0, 0, 0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = 'none';
        });
    });

    // EmailJS Configuration
    // Initialize EmailJS with your public key
    emailjs.init("ooggSqM8FuBbgaqIE"); // Replace with your EmailJS public key
    
    // Form handling with EmailJS
    const contactForm = document.querySelector('.contact-form form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Basic form validation
            const inputs = this.querySelectorAll('input[required], select[required], textarea[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = '#ff6b6b';
                    
                    // Reset border color after 3 seconds
                    setTimeout(() => {
                        input.style.borderColor = '#ddd';
                    }, 3000);
                } else {
                    input.style.borderColor = '#d4af37';
                }
            });
            
            if (isValid) {
                // Get form data
                const formData = new FormData(this);
                const templateParams = {
                    from_name: formData.get('name') || this.querySelector('input[type="text"]').value,
                    from_email: formData.get('email') || this.querySelector('input[type="email"]').value,
                    service_type: formData.get('service') || this.querySelector('select').value,
                    message: formData.get('message') || this.querySelector('textarea').value,
                    to_email: 'srivonx@gmail.com'
                };
                
                const submitButton = this.querySelector('.cta-button');
                const originalText = submitButton.textContent;
                
                // Update button state
                submitButton.textContent = 'Sending...';
                submitButton.style.background = '#d4af37';
                submitButton.disabled = true;
                
                // Send email using EmailJS
                emailjs.send('service_qxkm6rj', 'template_akkwkkr', templateParams)
                    .then(function(response) {
                        console.log('Email sent successfully!', response.status, response.text);
                        
                        // Success feedback
                        submitButton.textContent = 'Message Sent!';
                        submitButton.style.background = '#28a745';
                        
                        // Reset form after success
                        setTimeout(() => {
                            submitButton.textContent = originalText;
                            submitButton.style.background = '#333';
                            submitButton.disabled = false;
                            contactForm.reset();
                            
                            // Reset all border colors
                            inputs.forEach(input => {
                                input.style.borderColor = '#ddd';
                            });
                        }, 2500);
                        
                    }, function(error) {
                        console.error('EmailJS Error:', error);
                        
                        // Error feedback
                        submitButton.textContent = 'Error - Try Again';
                        submitButton.style.background = '#ff6b6b';
                        
                        // Reset button after error
                        setTimeout(() => {
                            submitButton.textContent = originalText;
                            submitButton.style.background = '#333';
                            submitButton.disabled = false;
                        }, 3000);
                    });
            }
        });
    }

    // Parallax effect for hero section
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero');
        
        if (hero) {
            const rate = scrolled * -0.5;
            hero.style.transform = `translateY(${rate}px)`;
        }
    });

    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animateElements = document.querySelectorAll('.service-card, .location-card, .about-content, .contact-content');
    
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // CTA button hover effects
    const ctaButtons = document.querySelectorAll('.cta-button');
    
    ctaButtons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px)';
            this.style.boxShadow = '0 8px 20px rgba(0, 0, 0, 0.3)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.2)';
        });
    });

    // Price hover animation
    const priceElements = document.querySelectorAll('.price');
    
    priceElements.forEach(price => {
        price.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        price.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Mobile menu toggle (for future mobile optimization)
    const createMobileMenu = () => {
        const nav = document.querySelector('.navbar');
        const navMenu = document.querySelector('.nav-menu');
        
        if (window.innerWidth <= 768) {
            // Mobile menu logic can be added here
            console.log('Mobile view detected');
        }
    };

    // Check for mobile on load and resize
    createMobileMenu();
    window.addEventListener('resize', createMobileMenu);

    // Loading animation
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    
    window.addEventListener('load', function() {
        document.body.style.opacity = '1';
    });
});
