<template>
    <div class="homepage">
      <!-- Navbar -->
      <nav class="navbar">
        <div class="logo">FARM<span>TECH</span></div>
        <ul class="nav-links">
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Services</a></li>
          <li><a href="#">Products</a></li>
          <li><a href="#">Farming Practices</a></li>
          <li><a href="#">News</a></li>
          <li><a href="#">Contact</a></li>
          <li><router-link to="/login">Login</router-link></li>
        </ul>
        <div class="icons">
          <i class="fas fa-search"></i>
          <i class="fas fa-shopping-cart"></i>
        </div>
      </nav>
  
      <!-- Hero Section -->
      <section class="hero">
        <div class="hero-content">
          <h1>The Future of Agriculture Starts Here</h1>
          <p>
            Discover how our innovative solutions are transforming the agriculture industry. 
            From cutting-edge technology to sustainable practices, we're paving the way for the future.
          </p>
          <button class="cta-button">Learn More</button>
        </div>
      </section>
  
      <!-- Footer Section -->
      <footer class="footer">
        <div class="footer-content">
          <div class="footer-section about">
            <h2>About Us</h2>
            <p>FARMTECH is dedicated to advancing agriculture through innovative solutions and sustainable practices.</p>
          </div>
          <div class="footer-section links">
            <h2>Quick Links</h2>
            <ul>
              <li><a href="#">Home</a></li>
              <li><a href="#">About</a></li>
              <li><a href="#">Services</a></li>
              <li><a href="#">Products</a></li>
              <li><a href="#">Contact</a></li>
            </ul>
          </div>
          <div class="footer-section contact">
            <h2>Contact Us</h2>
            <p><i class="fas fa-phone"></i> +123 456 789</p>
            <p><i class="fas fa-envelope"></i> info@farmtech.com</p>
            <p><i class="fas fa-map-marker-alt"></i> 123 Agriculture St., City, Country</p>
          </div>
          <div class="footer-section social">
            <h2>Follow Us</h2>
            <div class="social-icons">
              <i class="fab fa-facebook-f"></i>
              <i class="fab fa-twitter"></i>
              <i class="fab fa-instagram"></i>
              <i class="fab fa-linkedin-in"></i>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>&copy; 2024 FARMTECH | Designed by YourCompany</p>
        </div>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    name: "HomePage",
  };
  </script>
  
  <style scoped>
  /* Navbar Styles */
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: #7ac142;
  }
  
  .logo span {
    color: #000;
  }
  
  .nav-links {
    list-style: none;
    display: flex;
    gap: 1rem;
  }
  
  .nav-links a {
    text-decoration: none;
    color: #333;
    font-weight: 500;
  }
  
  .icons {
    font-size: 1.2rem;
    color: #333;
    display: flex;
    gap: 1rem;
  }
  
  /* Hero Section Styles */
  .hero {
    background-image: url('https://example.com/tractor.jpg');
    background-size: cover;
    background-position: center;
    padding: 6rem 2rem;
    color: #ffffff;
    text-align: center;
    position: relative;
  }
  
  .hero::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1;
  }
  
  .hero-content {
    position: relative;
    z-index: 2;
    max-width: 600px;
    margin: 0 auto;
  }
  
  .hero h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  
  .hero p {
    font-size: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .cta-button {
    background-color: #7ac142;
    color: #fff;
    padding: 0.8rem 2rem;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .cta-button:hover {
    background-color: #5a9b32;
  }
  
  /* Footer Styles */
  .footer {
    background-color: #333;
    color: #ffffff;
    padding: 2rem 1rem;
  }
  
  .footer-content {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
  }
  
  .footer-section {
    flex: 1;
    min-width: 200px;
    margin-bottom: 1rem;
  }
  
  .footer-section h2 {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
  }
  
  .footer-section p,
  .footer-section ul,
  .footer-section li {
    font-size: 0.9rem;
  }
  
  .footer-section ul {
    list-style: none;
    padding: 0;
  }
  
  .footer-section li {
    margin-bottom: 0.3rem;
  }
  
  .footer-section a {
    color: #ffffff;
    text-decoration: none;
    transition: color 0.3s;
  }
  
  .footer-section a:hover {
    color: #7ac142;
  }
  
  .footer-bottom {
    text-align: center;
    font-size: 0.8rem;
    padding-top: 1rem;
    border-top: 1px solid #555;
  }
  
  .social-icons {
    display: flex;
    gap: 0.5rem;
  }
  
  .social-icons i {
    font-size: 1.2rem;
    cursor: pointer;
    transition: color 0.3s;
  }
  
  .social-icons i:hover {
    color: #7ac142;
  }
  </style>  