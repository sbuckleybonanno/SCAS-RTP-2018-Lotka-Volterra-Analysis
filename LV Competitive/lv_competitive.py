import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


class LVModel(object):
    def __init__(self, alpha=1, beta=1, gamma=1, delta=1, Kx=1, Ky=1):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.Kx = Kx
        self.Ky = Ky

    def iterate(self, initial_x, initial_y, iterations, step_length):
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.iterations = iterations
        self.step_length = step_length

        x = initial_x
        y = initial_y
        self.x_data = [initial_x]
        self.y_data = [initial_y]
        
        for i in range(iterations):
            x, y = self.step(x, y)

    def step(self, x, y):
        dx_dt = ( self.alpha*x*(1 - ((x + self.beta*y)/(self.Kx))) ) * self.step_length # This and the next line represent the Lotka-Volterra model itself! 
        dy_dt = ( self.gamma*y*(1 - ((y + self.delta*x)/(self.Ky))) ) * self.step_length
        x = x + dx_dt
        y = y + dy_dt
        self.x_data.append(x)
        self.y_data.append(y)
        return x, y

    def plot(self, slider_interval):
        print("{0}, {1}, {2}, {3}".format(self.alpha, self.beta, self.gamma, self.delta))

        self.fig = plt.figure()

        self.x_line, = plt.plot(self.x_data)
        self.y_line, = plt.plot(self.y_data)

        plt.ylim(0,10)

        self.fig.subplots_adjust(bottom=0.45)

        ax_alpha = plt.axes([0.25, 0.35, 0.65, 0.03])
        ax_beta = plt.axes([0.25, 0.3, 0.65, 0.03])
        ax_gamma = plt.axes([0.25, 0.25, 0.65, 0.03])
        ax_delta = plt.axes([0.25, 0.2, 0.65, 0.03])
        ax_Kx = plt.axes([0.25, 0.15, 0.65, 0.03])
        ax_Ky = plt.axes([0.25, 0.1, 0.65, 0.03])

        s_alpha = Slider(ax_alpha, 'Alpha', 0, 2.0, valinit=self.alpha)
        s_beta = Slider(ax_beta, 'Beta', 0, 2.0, valinit=self.beta)
        s_gamma = Slider(ax_gamma, 'Gamma', 0, 2.0, valinit=self.gamma)
        s_delta = Slider(ax_delta, 'Delta', 0, 2.0, valinit=self.delta)
        s_Kx = Slider(ax_Kx, "Kx", 0, 20.0, valinit=self.Kx)
        s_Ky = Slider(ax_Ky, "Ky", 0, 20.0, valinit=self.Ky)
        
        s_alpha.on_changed(self.updateAlpha)
        s_beta.on_changed(self.updateBeta)
        s_gamma.on_changed(self.updateGamma)
        s_delta.on_changed(self.updateDelta)
        s_Kx.on_changed(self.updateKx)
        s_Ky.on_changed(self.updateKy)
       
        plt.show()

    def redraw(self):
        self.x_data = [self.initial_x]
        self.y_data = [self.initial_y]
        x = self.initial_x
        y = self.initial_y
        for i in range(self.iterations):
            x, y = self.step(x, y)
        self.x_line.set_ydata(self.x_data)
        self.y_line.set_ydata(self.y_data)
        self.fig.canvas.draw_idle()

    def updateAlpha(self, val):
        self.alpha = val
        self.redraw()

    def updateBeta(self, val):
        self.beta = val
        self.redraw()

    def updateGamma(self, val):
        self.gamma = val
        self.redraw()

    def updateDelta(self, val):
        self.delta = val
        self.redraw()

    def updateKx(self, val):
        self.Kx = val
        self.redraw()

    def updateKy(self, val):
        self.Ky = val
        self.redraw()

alpha = 1.0
beta = 1.0
gamma = 1.0
delta = 1.0

Kx = 10
Ky = 10

initial_x = 0.5
initial_y = 0.5
iterations = 10000
step_length = 0.01

slider_interval = 0.1

model = LVModel(alpha, beta, gamma, delta, Kx, Ky)
model.iterate(initial_x, initial_y, iterations, step_length)
model.plot(slider_interval)
