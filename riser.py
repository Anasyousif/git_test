def new_resizer(max_width, max_height):
    def inner_func(min_width=0, min_height=0):
        # Step 1: Validation
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def inner_most(width, height):
            # Step 2: Clamp Width
            # Increase if below min, then reduce if above max
            width = max(width, min_width)
            width = min(width, max_width)

            # Step 3: Clamp Height
            # Increase if below min, then reduce if above max
            height = max(height, min_height)
            height = min(height, max_height)

            # Step 4: Return the final dimensions
            return width, height

        # Step 5: Return the innermost function (the "worker")
        return inner_most

    # Step 6: Return the middle function (the "setter")
    return inner_func