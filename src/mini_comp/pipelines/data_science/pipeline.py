from kedro.pipeline import Pipeline, node, pipeline

from .nodes import write_output_file, wrapper_split_data, wrapper_get_best_model, wrapper_plot_fitted_values


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=wrapper_split_data,
                inputs=["sj_data", "iq_data"],
                outputs=["sj_train", "sj_test", "iq_train", "iq_test"],
                name="split_data_node",
            ),
            node(
                func=wrapper_get_best_model,
                inputs=["sj_train", "sj_test", "iq_train", "iq_test"],
                outputs=["sj_fitted_model", "iq_fitted_model"],
                name="get_best_model_node",
            ),
            node(
                func=wrapper_plot_fitted_values,
                inputs=["sj_train", "sj_fitted_model",
                        "iq_train", "iq_fitted_model"],
                outputs=['sj_figs', 'iq_figs'],
                name="plot_fitted_values_node",
            ),
            node(
                func=write_output_file,
                inputs=["sj_test", "iq_test",
                        "sj_best_model", "iq_best_model"],
                outputs="submission",
                name="write_output_file_node",
            ),

        ]
    )
