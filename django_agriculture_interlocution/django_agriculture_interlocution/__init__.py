import os
import logging
from django.db import connections

# 配置日志设置(标准化日志格式)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

# 检查是否加载了正确的Django配置
if os.getenv("DJANGO_SETTINGS_MODULE"):
    logger.info(f"Using settings: {os.getenv('DJANGO_SETTINGS_MODULE')}")

# 检查数据库连接状态
def check_database_connection():
    try:
        connections['default'].cursor()  # 测试数据库连接
        logger.info("Database connection is active.")
    except Exception as e:
        logger.error(f"Database connection error: {e}")

check_database_connection()