import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


class LVModel(object):
    def __init__(self, alpha=1, beta=1, gamma=1, delta=1):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.delta = delta

    def iterate(self, initial_x, initial_y, iterations, step_length):
        # self.initial_x = initial_x
        # self.initial_y = initial_y
        self.iterations = iterations
        self.step_length = step_length

        self.x_datas = []
        self.y_datas = []

        # Sorry this is hardcoded
        for i in range(10):
            initial_x = (i+1)/10
            initial_y = (i+1)/10

            x = initial_x
            y = initial_y
            self.x_data = [initial_x] # x_data and y_data are now temporary variables
            self.y_data = [initial_y]
        
            for i in range(iterations):
                x, y = self.step(x, y)

            self.x_datas.append(self.x_data)
            self.y_datas.append(self.y_data)

    def step(self, x, y):
        dx_dt = (self.alpha-self.beta*x*y) * self.step_length # This and the next line represent the Lotka-Volterra model itself! 
        dy_dt = (self.gamma*x*y-self.delta*y) * self.step_length
        x = x + dx_dt
        y = y + dy_dt
        self.x_data.append(x)
        self.y_data.append(y)
        return x, y

    def plot(self, slider_interval):
        print("{0}, {1}, {2}, {3}".format(self.alpha, self.beta, self.gamma, self.delta))

        self.fig = plt.figure()

        for i in range(len(self.x_datas)):
            self.line, = plt.plot(self.x_datas[i], self.y_datas[i])
        # self.y_line, = plt.plot(self.y_data)

        # plt.xlim(0, 4)
        # plt.ylim(0, 4)

        dotted_line_x = []
        dotted_line_y = []
        for i in range(0, 11):
            dotted_line_x.append(i/10)
            dotted_line_y.append(i/10)
        plt.plot(dotted_line_x, dotted_line_y, linestyle="dotted")

        # self.fig.subplots_adjust(bottom=0.35)

        # ax_alpha = plt.axes([0.25, 0.25, 0.65, 0.03])
        # ax_beta = plt.axes([0.25, 0.2, 0.65, 0.03])
        # ax_gamma = plt.axes([0.25, 0.15, 0.65, 0.03])
        # ax_delta = plt.axes([0.25, 0.1, 0.65, 0.03])

        # s_alpha = Slider(ax_alpha, 'Alpha', 0, 2.0, valinit=self.alpha)
        # s_beta = Slider(ax_beta, 'Beta', 0, 2.0, valinit=self.beta)
        # s_gamma = Slider(ax_gamma, 'Gamma', 0, 2.0, valinit=self.gamma)
        # s_delta = Slider(ax_delta, 'Delta', 0, 2.0, valinit=self.delta)
        
        # s_alpha.on_changed(self.updateAlpha)
        # s_beta.on_changed(self.updateBeta)
        # s_gamma.on_changed(self.updateGamma)
        # s_delta.on_changed(self.updateDelta)
       

        plt.show()

    def redraw(self):
        # self.x_data = [self.initial_x]
        # self.y_data = [self.initial_y]
        # x = self.initial_x
        # y = self.initial_y
        # for i in range(self.iterations):
        #     x, y = self.step(x, y)
        # self.line.set_xdata(self.x_data)
        # self.line.set_ydata(self.y_data)
        # self.fig.canvas.draw_idle()
        return None

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

alpha = 0.66666666
beta = 1.3333333
gamma = 1
delta = 1

initial_x = 0.5
initial_y = 0.5
iterations = 1000000
# iterations = 2000
step_length = 0.0001

slider_interval = 0.1

model = LVModel(alpha, beta, gamma, delta)
model.iterate(initial_x, initial_y, iterations, step_length)
model.plot(slider_interval)
