# %%
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


# %% [markdown]
# Write a function that provides an efficient look up of whether the user is in a group.
# 

# %%

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
      return True

    groups = group.get_groups()
    
    for i in groups:
        return is_user_in_group(user, i)
            


    return False

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3

# %%
is_user_in_group("sub_child_user", sub_child )

# %%
is_user_in_group("sub_child_user", child )

# %%
is_user_in_group("sub_child_user", parent )

# %%
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print("Test Case 1: User in nested group")
print(is_user_in_group(sub_child_user, parent))  
# expoected : True

# %%
empty_group = Group("empty")

print("\nTest Case 2: Empty group")
print(is_user_in_group("some_user", empty_group)) 
 # Expected: False

# %%
parent.add_user("valid_user")

print("\nTest Case 3: None user")
print(is_user_in_group(None, parent))
  # Expected: False


