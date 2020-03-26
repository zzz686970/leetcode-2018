/*
a tree structure is stored inside a table,need to separate root, inner and leaf node
node, parent_node

select node, case when parent_node is null then root,
				when exists(select parent_node from bst b where a.node=b.parent_node) then 'inner'
				else 'leaf' end as tree_type
				from bst a
				order by node
 */