from PassiveTreeNode import *

class PassiveTree:
  """
    This class holds the root nodes of the Passive Tree, and has utility functions for working with
    a passive tree.
  """

  def __init__(self):
    self.agilityRoot = None ## The agility root node.
    self.strengthRoot = None ## The strength root node.
    self.wisdomRoot = None ## The wisdom root node.
    self.constitutionRoot = None ## The constitution root node.

  ## Add method to parse a hero's tree from however we represent it in the model.
  ## Add method

## Common Node Attributes
## Agility
BaseAgilityNode = {'agility': 5}
LargeAgilityNode = {'agility': 15}

## Action Speed
BaseActionSpeedNode = {'actionrate': 2}

## Dagger Damage
BaseDaggerDamage = {'daggerdamage': 8}

## Bow Damage
BaseBowDamage = {'bowdamage': 8}

## XBow Damage
BaseXBowDamage = {'xbowdamage': 8}

## The empty (no nodes picked) Passive Tree Layout
## Agility Section
AgilityRoot = PassiveTreeNode(BaseAgilityNode, 1)
## Branch, 2 choices, agi or actionspeed
AgilityBranch1 = PassiveTreeNode(BaseAgilityNode, 2)
AgilityBranch2 = PassiveTreeNode(BaseActionSpeedNode, 3)
## agi branch, 3 nodes (inlcuding the first one)
AgilityRoot.create_links([AgilityBranch1, AgilityBranch2])
AgilityBranch1Step2 = PassiveTreeNode(BaseAgilityNode, 4)
AgilityBranch1.create_link(AgilityBranch1Step2)
AgilityBranch1Step3 = PassiveTreeNode(BaseAgilityNode, 5)
AgilityBranch1Step2.create_link(AgilityBranch1Step3)
## actionspeed branch, 3 nodes (including the first one)
AgilityBranch2Step2 = PassiveTreeNode(BaseActionSpeedNode, 6)
AgilityBranch2.create_link(AgilityBranch2Step2)
AgilityBranch2Step3 = PassiveTreeNode(BaseActionSpeedNode, 7)
AgilityBranch2Step2.create_link(AgilityBranch2Step3)
## actionspeed and agi branches converge
AgilityKeyNode1 = PassiveTreeNode(LargeAgilityNode, 8)
AgilityKeyNode1.create_links([AgilityBranch2Step3, AgilityBranch1Step3])
## Branch, 3 choices, dagger (towards wis), bow (towards deep agi), xbow (towards str)
DaggerBranch = PassiveTreeNode(BaseDaggerDamage, 9)
BowBranch = PassiveTreeNode(BaseBowDamage, 10)
XBowBranch = PassiveTreeNode(BaseXBowDamage, 11)
AgilityKeyNode1.create_links([DaggerBranch, BowBranch, XBowBranch])

## Strength Section
# StrengthRoot = PassiveTreeNode()

# ## Wisdom Section
# WisdomRoot = PassiveTreeNode()

# ## Constitution Section
# ConstitutionRoot = PassiveTreeNode()

## Temporary
visited = []
def dfs(node):
  visited.append(node)
  print node.nodeId
  for link in node.links:
    if link not in visited:
      dfs(link)

print dfs(AgilityRoot)
