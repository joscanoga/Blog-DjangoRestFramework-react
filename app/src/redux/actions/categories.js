import { Axios } from "axios";
import { GET_CATEGORIES_FAIL, GET_CATEGORIES_SUCCESS } from "./types";

export const get_Categories = () => async dispatch => {
    const config = {
        headers: {
            'Accept': 'application/json',}

    }
    try {
        const res = await Axios.get(`${process.env.REACT_APP_API_URL}/api/cotegory/categories`, config);
    }
};