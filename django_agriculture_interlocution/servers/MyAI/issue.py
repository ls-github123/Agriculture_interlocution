# 导入通义大模型
from langchain_community.llms import Tongyi
# 导入模板类
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# sy = SystemMessage(content="你是一个农业专家. 你的名字叫宋专家.")
# hu = HumanMessage(content="我家小麦生长缓慢？")
# message = [sy, hu]


def issue(species):
        # 定义模板
        message = [
                ("system", "假设你是一位农业方面的专家，非常擅长农作物方面"),
                ("human", "我的问题是{species}，请帮我提几个建议"),
        ]

        # 实例化模板类
        chartmp = ChatPromptTemplate.from_messages(message)
        prompt = chartmp.format_messages(species=species)
        print("Generated Prompt:",prompt)

        # 实例化通义大模型
        tongyi = Tongyi()
        ret = tongyi.invoke(prompt)
        print("Model Response:",ret)
        print(type(ret))
        return ret


