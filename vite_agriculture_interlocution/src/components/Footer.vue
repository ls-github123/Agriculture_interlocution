<!--底部Footer组件封装-->
<template>
    <footer class="footer">
        <div class="footer-content">
            <div class="footer-section about">
                <h2>关于我们</h2>
                <P>MAP智慧农业 致力于通过创新解决方案和可持续实践推动农业发展.</P>
            </div>
            <div class="footer-section links">
                <h2>快速访问</h2>
                <ul>
                    <li><a href="#">首页</a></li>
                    <li><a href="#">关于</a></li>
                    <li><a href="#">服务</a></li>
                    <li><a href="#">产品</a></li>
                    <li><a href="#">联系我们</a></li>
                </ul>
            </div>
            <div class="footer-section contact">
                <h2>联系我们</h2>
                <p><i class="fas fa-phone"></i>+86 18795190581</p>
                <p><i class="fas fa-envelope"></i> Lpsserver443@outlook.com</p>
                <p><i class="fas fa-map-marker-alt"></i>123 Agriculture St., City, Country</p>
            </div>
            <div class="footer-section social">
                <h2>找到我们</h2>
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
</template>

<script>
export default {
    name: 'Footer',
};
</script>

<style scoped>
.footer {
  background-color: #333;
  color: #fff;
  padding: 20px 0;
  font-family: Arial, sans-serif;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.footer-section {
  flex: 1;
  padding: 0 20px;
}

.footer-section h2 {
  font-size: 18px;
  margin-bottom: 10px;
}

.footer-section p, .footer-section ul, .footer-section ul li, .footer-section ul li a {
  font-size: 14px;
  color: #fff;
  text-decoration: none;
}

.footer-section ul {
  list-style: none;
  padding: 0;
}

.footer-section ul li {
  margin-bottom: 8px;
}

.footer-section ul li a:hover {
  color: #ffdd57;
}

.social-icons i {
  font-size: 18px;
  margin-right: 10px;
  cursor: pointer;
  color: #fff;
}

.social-icons i:hover {
  color: #ffdd57;
}

.footer-bottom {
  text-align: center;
  padding: 10px 0;
  background-color: #222;
  font-size: 12px;
}
</style>