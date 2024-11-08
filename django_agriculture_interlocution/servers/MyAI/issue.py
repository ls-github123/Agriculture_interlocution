# 导入通义大模型
from langchain_community.llms import Tongyi
# 导入模板类
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# sy = SystemMessage(content="你是一个农业专家. 你的名字叫宋专家.")
# hu = HumanMessage(content="我家小麦生长缓慢？")
# message = [sy, hu]


def issue(species_dict):

     try:   
        # 定义模板
        message = [
                SystemMessage(content="假设你是一位农业方面的专家，非常擅长农作物方面"),
                HumanMessage(content=f"我的问题是{species_dict['species']}，请帮我提几个建议"),
        ]

        # 实例化模板类
        chartmp = ChatPromptTemplate.from_messages(message)
        prompt = chartmp.format_messages(species=species_dict['species'])
        print("Generated Prompt:",prompt)
        print("Type of prompt:", type(prompt))

        # 将 prompt 转换为字符串
        prompt_str = "\n".join([msg.content for msg in prompt])
        print("Converted prompt string:", prompt_str)

        # 实例化通义大模型
        tongyi = Tongyi(api_key="sk-7120502d21944e6db08732969adae8a6")
        # 调用模型
        
        ret = tongyi.invoke(prompt_str)
        print("Model Response:", ret)
        print("Type of model response:", type(ret))

        return ret 
     except KeyError as e:
        print(f"KeyError occurred: {e}")
        raise   
     except Exception as e:
        print(f"Error invoking model: {e}")
        raise


