import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.graph_size, 9)
        self.assertEqual(g.get_vertices(), ["1","2","3","4","5","6","7","8","9"])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())
    
    def test_03_init(self):
        g = Graph('test1.txt')
        self.assertEqual(g.graph_size, 9)
        self.assertEqual(g.get_vertices(), ["1","2","3","4","5","6","7","8","9"])
    
    def test_04_add_vert(self):
        g = Graph()
        g.add_vertex(4)
        g.add_vertex(14)
        g.add_vertex(24)
        g.add_vertex(34)
        self.assertEqual(g.graph_size, 4)
        self.assertEqual(g.get_vertices(), [4,14,24,34])
    
    def test_05_get_vert(self):
        g = Graph()
        g.add_vertex(4)
        g.add_vertex(14)
        g.add_vertex(24)
        g.add_vertex(34)
        self.assertEqual(g.get_vertices(), [4,14,24,34])
        vtx1 = g.get_vertex(4)
        self.assertEqual(vtx1.id, 4)
        vtx2 = g.get_vertex(14)
        self.assertEqual(vtx2.id, 14)
        vtx3 = g.get_vertex(24)
        self.assertEqual(vtx3.id, 24)
        
    def test_06_add_edge(self):
        g = Graph()
        g.add_vertex(4)
        g.add_vertex(14)
        g.add_vertex(24)
        g.add_vertex(34)
        g.add_edge(4,14)
        g.add_edge(4,24)
        g.add_edge(4,34)
        g.add_edge(14,24)
        vtx = g.get_vertex(4)
        self.assertEqual(len(vtx.adjacent_to), 3)
        vtx = g.get_vertex(14)
        self.assertEqual(len(vtx.adjacent_to), 2)
        vtx = g.get_vertex(24)
        self.assertEqual(len(vtx.adjacent_to), 2)
        vtx = g.get_vertex(34)
        self.assertEqual(len(vtx.adjacent_to), 1)
    
    def test_07_get_veticies(self):
        g = Graph()
        g.add_vertex(19)
        g.add_vertex(10)
        self.assertEqual(g.get_vertices(), [10,19])
        g.add_vertex(2)
        self.assertEqual(g.get_vertices(), [2,10,19])
        g.add_vertex(24)
        self.assertEqual(g.get_vertices(), [2,10,19,24])

if __name__ == '__main__':
   unittest.main()
