#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ast

code = """
def greet(name):
    print("Hello, " + name)

greet("World")
"""

parsed_ast = ast.parse(code)
for node in ast.walk(parsed_ast):
    print(node.__class__.__name__)
def find_function_names(node):
    if isinstance(node, ast.FunctionDef):
        print(f"Function Name: {node.name}")

# Traverse and analyze
for node in ast.walk(parsed_ast):
    find_function_names(node)
new_code = """
def greet(name):
    print("Hello, " + name)

greet("World")
"""

new_parsed_ast = ast.parse(new_code)

# Modify the AST
for node in ast.walk(new_parsed_ast):
    if isinstance(node, ast.FunctionDef):
        node.body.insert(0, ast.parse("print('Function Executed')").body[0])

# Compile the modified AST
modified_code = compile(new_parsed_ast, filename='', mode='exec')
exec(modified_code)
from graphviz import Digraph

def build_ast_graph(dot, node, parent_name=""):
    current_name = parent_name + node.__class__.__name__
    dot.node(current_name, label=node.__class__.__name__)

    for child_node in ast.iter_child_nodes(node):
        child_name = build_ast_graph(dot, child_node, current_name)
        dot.edge(current_name, child_name)

    return current_name

# # Create a directed graph
# dot = Digraph(comment='AST Visualization')
#
# # Build and visualize the AST graph
# build_ast_graph(dot, parsed_ast)
# dot.render('ast_visualization', format='png', cleanup=True, view=True)
#
#
# # In[ ]:




