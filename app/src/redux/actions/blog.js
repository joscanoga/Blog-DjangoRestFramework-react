import axios from 'axios';
import {GET_BLOG_LIST_SUCCESS,GET_BLOG_LIST_FAIL,GET_BLOG_SUCCESS,GET_BLOG_FAIL, } from './types';

export const getBlogList = () => async dispatch => {
    const config = {
        headers: {
        'Accept': 'application/json',
        }
    };
    try {
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/blog/`, config);
        if (res.status === 200) {
            dispatch({
                type: GET_BLOG_LIST_SUCCESS,
                payload: res.data
            });
        }
        else {
            dispatch({
                type: GET_BLOG_LIST_FAIL
            });
        }

    }
    catch (err) {}
};
export const getBlogList_page = (p) => async dispatch => {
    const config = {
        headers: {
        'Accept': 'application/json',
        }
    };
    try {
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/blog/?p=${p}`, config);
        if (res.status === 200) {
            dispatch({
                type: GET_BLOG_LIST_SUCCESS,
                payload: res.data
            });
        }
        else {
            dispatch({
                type: GET_BLOG_LIST_FAIL
            });
        }

    }
    catch (err) {}
};

export const getBlog = (slug) => async dispatch => {
    const config = {
        headers: {
        'Accept': 'application/json',
        }
    };
    try {
        const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/blog/${slug}`, config);
        if (res.status === 200) {
            dispatch({
                type: GET_BLOG_SUCCESS,
                payload: res.data
            });
        }
        else {
            dispatch({
                type: GET_BLOG_FAIL
            });
        }

    }
    catch (err) {}

}