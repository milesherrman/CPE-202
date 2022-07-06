from queue_array2 import * #Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.bipartite = 0
        self.visited = False


class Graph:
   
    def __init__(self, filename = None):
        self.vtx_list = []
        self.id_list = []
        self.graph_size = 0
        
        if filename != None:
            graph_file = open(filename, "r")
            for line in graph_file:
                current = line.split()
                self.add_vertex(current[0])
                if len(current) > 1:
                    self.add_vertex(current[1])
                    self.add_edge(current[0], current[1])
            graph_file.close()
        
    def add_vertex(self, key):
        '''Add a vertex with id key into the graph'''
        if key not in self.id_list:
            self.vtx_list.append(Vertex(key))
            self.id_list.append(key)
            self.graph_size = self.graph_size + 1

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        for vtx in self.vtx_list:
            if vtx.id == key:
                return vtx
        return None
    
    def add_edge(self, v1, v2):
        '''Adds an edge between verticies with IDs v1 and v2'''
        vtx1 = self.get_vertex(v1)
        vtx2 = self.get_vertex(v2)
        if vtx2 not in vtx1.adjacent_to:
            vtx1.adjacent_to.append(vtx2)
        if vtx1 not in vtx2.adjacent_to:
            vtx2.adjacent_to.append(vtx1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        sorted = self.id_list
        sorted.sort()
        return sorted

    def conn_components(self): 
        '''Returns a list of lists'''
        final = []
        verticies = self.get_vertices()
        for id in verticies:
            vertex = self.get_vertex(id)
            if vertex.visited == False:
                connected = self.depth_first_search(vertex, ["v" + vertex.id])
                final.append(connected)
        for vtx in self.vtx_list:
            vtx.visited = False
        for lst in final:
            lst.sort()
        return final
                
        
    def depth_first_search(self, vertex, current):
        vertex.visited = True
        next_vert = [vtx for vtx in vertex.adjacent_to if not vtx.visited]
        for vtx in next_vert:
            if vtx.visited == False:
                current.append("v" + vtx.id)
                self.depth_first_search(vtx, current)
        return current
            

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.'''
        for vtx in self.vtx_list:
            if self.breadth_first_search(vtx) == False:
                return False
        return True
    
    def breadth_first_search(self, vertex):
        for vtx in self.vtx_list:
            vtx.visited = False
            vtx.bipartite = 0
        queue = Queue(40)
        vertex.bipartite = 1
        queue.enqueue(vertex)
        prev = 1
        while not queue.is_empty():
            if vertex.visited == False:
                vertex.visited = True
                next_vert = [vert.id for vert in vertex.adjacent_to]
                next_vert.sort()
                prev = vertex.bipartite
                for id in next_vert:
                    vtx = self.get_vertex(id)
                    if vtx.bipartite == 0:
                        if prev == 1:
                            vtx.bipartite = 2
                        else:
                            vtx.bipartite = 1
                    else:
                        if vtx.bipartite == prev:
                            return False
                    queue.enqueue(vtx)
            try:
                vertex = queue.dequeue()
            except:
                pass
        return True
