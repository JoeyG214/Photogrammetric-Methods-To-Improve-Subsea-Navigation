class DetectedObject:
    def __init__(self, object_id, bounding_box, depth, timestamp):
        self.object_id = object_id
        self.bounding_box = bounding_box # Tuple of (x, y, width, height)
        self.depth = depth # Estimated distance from camera
        self.timestamp = timestamp # Timestamp when the object was detected

        self.positions = [(self.get_centroid(), depth, timestamp)] # List of positions over time

    def get_centroid(self):
        x, y, width, height = self.bounding_box
        return (x + width / 2, y + height / 2)
    
    def update(self, bounding_box, depth, timestamp):
        self.bounding_box = bounding_box
        self.depth = depth
        self.timestamp = timestamp
        self.positions.append((self.get_centroid(), depth, timestamp))

    def get_speed(self):
        if len(self.positions) < 2:
            return None  # Can't calculate speed with less than 2 positions

        # Get the last two positions
        (x1, y1, z1, t1), (x2, y2, z2, t2) = self.positions[-2:]

        # Calculate Euclidean distance between the two positions
        delta_d = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5

        # Calculate time difference in seconds
        delta_t = (t2 - t1).total_seconds()

        # Calculate speed
        speed = delta_d / delta_t

        return speed