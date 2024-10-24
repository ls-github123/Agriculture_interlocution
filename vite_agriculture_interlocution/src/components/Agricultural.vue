<!-- src/components/FindMachinery.vue -->
<template>
    <div>
        <h1>找农机</h1>
        <form @submit.prevent="handleSubmit">
            <input type="text" v-model="serviceTime" placeholder="请输入期望服务时间">
            <input type="text" v-model="serviceLocation" placeholder="请输入服务地点">
            <select v-model="selectedService">
                <option value="">请选择作业内容</option>
                <option v-for="(service, index) in services" :key="index" :value="service.id">{{ service.name }}</option>
            </select>
            <button type="submit">发布作业订单</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            serviceTime: '',
            serviceLocation: '',
            selectedService: '',
            services: [],
        };
    },
    methods: {
        async handleSubmit() {
            // 发送 POST 请求到后端
            const response = await axios.post('http://localhost:8000/', {
                service_time: this.serviceTime,
                service_location: this.serviceLocation,
                service_id: this.selectedService,
            });
            console.log(response.data);
        },
        async fetchServices() {
            const response = await axios.get('http://localhost:8000/');
            this.services = response.data;
        },
    },
    mounted() {
        this.fetchServices();
    },
};
</script>
