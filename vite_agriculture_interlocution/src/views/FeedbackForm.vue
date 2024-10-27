<template>
  <div class="feedback-form-container">
    <div class="header">
      <button class="back-btn" @click="goBack">
        <i class="fas fa-arrow-left"></i>
      </button>
      <h1>意见反馈</h1>
    </div>
    
    <!-- 上传图片部分 -->
    <div class="section">
      <div class="section-header">
        <label>请提供相关问题截图或视频，最多3个</label>
      </div>
      <div class="upload-section">
        <label for="file-upload" class="file-label">
          <img src="/images/upload.gif" alt="上传" class="upload-icon" />
        </label>
        <input id="file-upload" type="file" multiple accept="image/*" @change="handleImageUpload" />
        <div class="image-preview" v-if="images.length > 0">
          <img v-for="(image, index) in images" :key="index" :src="image" alt="上传的图片" class="preview-image" />
        </div>
      </div>
    </div>
    
    <!-- 反馈描述部分 -->
    <div class="section">
      <div class="section-header">
        <label>反馈描述</label>
      </div>
      <textarea id="description" placeholder="请在这里写下您的建议和意见" v-model="feedbackText"></textarea>
    </div>
    
    <!-- 问题类型部分 -->
    <div class="section">
      <div class="section-header">
        <label>问题类型</label>
      </div>
      <div class="issue-type">
        <button v-for="type in issueTypes" :key="type" @click="selectIssueType(type)" :class="{ selected: selectedType === type }">{{ type }}</button>
      </div>
    </div>
    
    <!-- 联系方式部分 -->
    <div class="section">
      <div class="section-header">
        <label>联系方式</label>
      </div>
      <div class="contact-info">
        <label for="username">联系人</label>
        <input type="text" id="username" v-model="username" disabled />
        <label for="phone">联系电话</label>
        <input type="tel" id="phone" v-model="phone" disabled />
      </div>
    </div>
    
    <button class="submit-btn" @click="submitFeedback">提交</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      feedbackText: '',
      selectedType: '',
      username: '用户1531',
      phone: '18736611531',
      issueTypes: ['功能建议', '页面问题', '操作问题', '功能问题', '购买问题', '其他'],
      images: [],
      files: [],
    };
  },
  methods: {
    handleImageUpload(event) {
      const files = event.target.files;
      const newImages = [];
      for (let i = 0; i < files.length; i++) {
        if (this.images.length < 3) {
          const file = files[i];
          const reader = new FileReader();
          reader.onload = (e) => {
            newImages.push(e.target.result);
            this.images = [...this.images, ...newImages];
          };
          reader.readAsDataURL(file);
        }
      }
    },
    selectIssueType(type) {
      this.selectedType = type;
    },
    submitFeedback() {
      if (!this.feedbackText) {
        alert('请填写反馈内容');
        return;
      }
      if (!this.selectedType) {
        alert('请选择问题类型');
        return;
      }
      alert('反馈已提交');
      this.$router.push('/messages');
    },
    goBack() {
      this.$router.push('/messages');
    },
  },
};
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

.feedback-form-container {
  width: 100%;
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background-color: rgb(255, 255, 255);
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.header .back-btn {
  display: inline-flex;
  align-items: center;
  padding: 10px 15px;
  background-color: #ffffff;
  color: #333;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.header .back-btn:hover {
  background-color: #dfe3e6;
}

.header h1 {
  font-size: 24px;
  margin: 0;
  color: #333;
  flex: 1;
  text-align: center;
}

.section {
  margin-bottom: 20px;
  text-align: left;
}

.section-header {
  margin-bottom: 10px;
  font-weight: bold;
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 5px;
}

.section-header label {
  font-size: 14px;
  color: #333;
}

.upload-section {
  margin-bottom: 20px;
  text-align: left;
}

.file-label {
  display: inline-flex;
  align-items: center;
  padding: 10px 20px;
  background-color: #fdfdfd;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.file-label img.upload-icon {
  margin-right: 5px;
  width: 24px;
  height: 24px;
  vertical-align: middle;
}



input[type="file"] {
  display: none;
}

.image-preview {
  margin-top: 10px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.preview-image {
  max-width: 100px;
  max-height: 100px;
  border-radius: 5px;
  object-fit: cover;
}

textarea {
  width: 100%;
  height: 150px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 20px;
  resize: vertical;
  font-size: 14px;
  color: #333;
}

.issue-type {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.issue-type button {
  margin: 5px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #f0f2f5;
  color: #333;
  cursor: pointer;
  transition: background-color 0.3s;
}


.contact-info {
  text-align: left;
  margin-bottom: 20px;
}

.contact-info label {
  display: block;
  margin-bottom: 5px;
  font-size: 14px;
  color: #333;
}

.contact-info input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
  font-size: 14px;
  color: #333;
}

.submit-btn {
  width: 100%;
  padding: 10px;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #218838;
}
</style>