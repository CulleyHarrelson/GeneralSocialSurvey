from util import Factory

if __name__ == '__main__':
    app = Factory.CustomDash()
    dashboard_1 = Factory.Dashboard()
    dashboard_1.add_figure_from_data_frame()  # When it's empty, add Dummy Data
    dashboard_1.add_figure_from_data_frame(figure_id="another_example")
    dashboard_1.add_figure_from_data_frame({
        "Category": ["Shelf", "Table", "Chair", "Shelf", "Table", "Chair"],  # First element is presumed to be x-axis
        "Amount": [4, 1, 2, 2, 4, 5],  # Second element be y-axis
        "City": ["CA", "CA", "CA", "NJ", "NJ", "NJ"]
    }, figure_id="data_frame_example")

    app.add_dashboard(dashboard_1)
    app.run_custom_server()
