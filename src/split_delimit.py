from textnode import TextNode
from enum import Enum
from enum_types import *

def split_nodes_delimiter(old_nodes: list[TextNode], 
                          delimiter: str,
                            text_type: Enum
                            ) -> list[TextNode]:
    """returns list of nodes, split into multiple nodes"""
    outputlist = []
    for old_node in old_nodes:
        if old_node.text_type != node_type.text:
            outputlist.append(old_node)
            continue
        try:
            text_length = len(old_node.text)
            index = old_node.text.index(delimiter)
            if index == -1:
                raise Exception("delimiter not present/invalid syntax")

        except Exception as e:
            print(f"Delimiter not found. Error: {e}")
        
        running_length = 0
        splitted_list = old_node.text.split(delimiter)
        for item in splitted_list:
            running_length += len(item)
            if running_length <= index:
                outputlist.append(TextNode(item, node_type.text))
            
                continue



        return outputlist
        """
        TextNode.text = text
		TextNode.text_type = text_type
		TextNode.url = url

        node_type = Enum('node_type',["text","bold","italic","code","link","image"])
        """