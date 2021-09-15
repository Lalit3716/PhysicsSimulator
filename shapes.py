import pymunk


class Box:
    def __init__(self, space, d1, d2, t=5, elasticity=0.999, friction=0.5) -> None:
        x1, y1 = d1
        x2, y2 = d2
        pts = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
        b0 = space.static_body
        for i in range(4):
            j = i + 1
            if j >= 4:
                j = 0
            segment = pymunk.Segment(b0, pts[i], pts[j], t)
            segment.elasticity = elasticity
            segment.friction = friction
            space.add(segment)


class Circle:
    def __init__(self, space, position, radius=20, elasticity=0.999, friction=0.5) -> None:
        self.body = pymunk.Body(mass=1, moment=10)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = elasticity
        self.shape.friction = friction
        space.add(self.body, self.shape)
