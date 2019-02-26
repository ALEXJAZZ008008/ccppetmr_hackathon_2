import matplotlib.pyplot
import pSTIR


def display_slice(input_slice):
    bitmap = matplotlib.pyplot.imshow(input_slice)
    matplotlib.pyplot.show()

    return bitmap


def display_data(input_data):
    array = input_data.as_array()

    for slice_number in range(array.shape[0]):
        display_slice(array[slice_number, :, :, ])

    return input_data


def backward_project(input_model, input_data):
    output_backward_data = display_data(input_model.backward(input_data))

    return output_backward_data


def forward_project(input_model, input_data):
    output_forward_data = display_data(input_model.forward(input_data))

    return output_forward_data


def simulate_data(input_data, scale):
    circle = pSTIR.EllipticCylinder()
    circle.set_length(scale * 5)
    circle.set_radii((1, 1))

    circle.set_origin((scale * 0, scale * 0, scale * 0))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 10, scale * 10, scale * 0))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 10, scale * 0, scale * 0))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 0, scale * 10, scale * 0))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * -10, scale * -10, scale * 0))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * -10, scale * 0, scale * 0))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 0, scale * -10, scale * 0))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * -10, scale * 10, scale * 0))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 10, scale * -10, scale * 0))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 0, scale * 0, scale * 10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 10, scale * 10, scale * 10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 10, scale * 0, scale * 10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 0, scale * 10, scale * 10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * -10, scale * -10, scale * 10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * -10, scale * 0, scale * 10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 0, scale * -10, scale * 10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * -10, scale * 10, scale * 10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 10, scale * -10, scale * 10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 0, scale * 0, scale * -10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 10, scale * 10, scale * -10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 10, scale * 0, scale * -10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 0, scale * 10, scale * -10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * -10, scale * -10, scale * -10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * -10, scale * 0, scale * -10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 0, scale * -10, scale * -10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * -10, scale * 10, scale * -10))
    input_data.add_shape(circle, 1)

    circle.set_origin((scale * 10, scale * -10, scale * -10))
    input_data.add_shape(circle, 1)

    return input_data


def main():
    acquisition_data = pSTIR.AcquisitionData("RATPET")
    image_data = acquisition_data.create_uniform_image(1.0)

    model = pSTIR.AcquisitionModelUsingRayTracingMatrix()
    model.set_up(acquisition_data, image_data)

    backward_data = display_data(simulate_data(image_data, 2.0))

    for i in range(1):
        forward_data = forward_project(model, backward_data)

        backward_data = backward_project(model, forward_data)


main()
