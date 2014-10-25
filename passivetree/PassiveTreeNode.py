## The passive node class
class PassiveTreeNode:
  """This class is used to represent a node in the passive skill tree"""

  ## The constructor for this class
  def __init__(self, attribute, nodeId):
    self.links = [] ## The list of other nodes that this node links to.
    self.attribute = attribute  ## What this node does.
    self.nodeId = nodeId ## This node's id.
    self.isPicked = False ## Whether or not the hero has picked this node.

  ## Add a link between this node and the given node.
  def create_link(self, node):
    ## All links are 2 way, so we add the link to both nodes here.
    node.links.append(self)
    self.links.append(node)

  def create_links(self, nodes):
    for node in nodes:
      self.create_link(node)


  