thickness = int(input()) # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    # Left side rjust, right side ljust to form the triangle
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    # Center the pillars within their specific widths
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    # Center the wide belt
    print((c*thickness*5).center(thickness*6))    

# Bottom Pillars
for i in range(thickness+1):
    # Same as Top Pillars
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))    

# Bottom Cone
for i in range(thickness):
    # Inner part forms the inverted triangle, then the whole thing is rjust to the end
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
