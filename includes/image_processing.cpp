#include <pybind11/numpy.h>

namespace py = pybind11;

void adjust_blackness(py::array_t<uint8_t> image, int threshold, int value)
{
    auto buf = image.request();
    uint8_t *ptr = static_cast<uint8_t *>(buf.ptr);
    int width = buf.shape[1];
    int height = buf.shape[0];

    for (int y = 0; y < height; ++y)
    {
        for (int x = 0; x < width; ++x)
        {
            int index = y * width * buf.itemsize + x * buf.itemsize;
            uint8_t *pixel = ptr + index;

            uint8_t r = pixel[0];
            uint8_t g = pixel[1];
            uint8_t b = pixel[2];
            uint8_t a = pixel[3];

            r = r * value / 100;
            g = g * value / 100;
            b = b * value / 100;

            if (r <= threshold && g <= threshold && b <= threshold)
            {
                pixel[0] = 0;
                pixel[1] = 0;
                pixel[2] = 0;
            }
            else
            {
                pixel[0] = r;
                pixel[1] = g;
                pixel[2] = b;
            }
        }
    }
}

PYBIND11_MODULE(image_processing, m)
{
    m.def("adjust_blackness", &adjust_blackness, "Adjust image blackness");
}