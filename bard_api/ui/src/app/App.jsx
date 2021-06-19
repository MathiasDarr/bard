import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import { Provider } from "react-redux";

import { inRange } from 'lodash';
import Router from './Router';

import store from './store'
import { endpoint } from './api';


import './App.scss'



function App() {
  // extends blueprint icon renderer to render icons from the ftm iconRegistry

  return (
    <Provider store={store}>
      
      <BrowserRouter>
        <Route path="/" component={Router} />
      </BrowserRouter>
    </Provider>
  
  );
}

export default App;
