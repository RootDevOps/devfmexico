import React from 'react';
import Home from './pages/Home';
import Login from './pages/login';
import  App from './App.js';



import {
  BrowserRouter as ReactRouter,
  Route,
} from 'react-router-dom';

export default class Router extends React.Component{

    render() {
      return (
        <ReactRouter>
          <App>
            <Route exact path="/" component={Home}></Route>
            <Route  path="/login" component={Login}></Route>
            <Route exact path="/Signup" component={Login}></Route>
          </App>
        </ReactRouter>
      );
    }
  }
