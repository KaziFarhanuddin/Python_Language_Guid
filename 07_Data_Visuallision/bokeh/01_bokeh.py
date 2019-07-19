from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y = [6, 7, 4, 5, 9]

output_file('Apple.html')

p = figure(title="Apple", x_axis_label="X axis", y_axis_label="Y axis")

p.line(x, y, legend="test", line_width=2)

show(p)
