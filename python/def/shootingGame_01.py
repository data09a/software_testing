class Gun:

    def __init__(self, model):
        # 1. gun model
        self.model = model

        # 2. bullet quantity
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1. check bullet quantity
        if self.bullet_count <= 0:
            print("[%s] there is no bullet..." % self.model)

            return

        # 2. start shooting, -1
        self.bullet_count -= 1

        # 3. shooting noise
        print("[%s] bang bang... [%d]" % (self.model, self.bullet_count))


# 1. create gun object
ak47 = Gun("AK47")

ak47.add_bullet(50)
ak47.shoot()
