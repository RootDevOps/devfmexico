import React from 'react';

import Title from '../components/Title';

import TextField from 'material-ui/TextField';

import RaisedButton from 'material-ui/RaisedButton';

import {BrowserRouter as ReactRouter, Link, Route} from 'react-router-dom';

export default class Login extends React.Component {

  render() {
    return (

      <div className="row ">
        <div className="col-xs-12 col-sm-6 ">
          <Title/>
          <div>
            <TextField floatingLabelText="Correo Electronico" type="email" className="TextField"/>
            <TextField floatingLabelText="Contraseña" type="password" className="TextField"/>

              <div className="Login-actions">

                <Route path="/login" exact render={() => {
                  return (
                    <div>
                  <RaisedButton linkbutton containerElement={<Link to="/signup" />} label="Crear Cuenta Nueva" primary={true}
                  style={{'margin-right': "1em", 'margin-bottom': "1em"}}/>
                      <RaisedButton label="Ingresar" secondary={true}/>
                    </div>
                  );
                }}></Route>

                <Route path="/signup" exact render={() => {
                  return (
                    <div>
                      <RaisedButton linkbutton containerElement={<Link to="/login" />} label="Ya tengo cuenta" primary={true}
                      style={{'margin-right': "1em", 'margin-bottom': "1em"}}/>
                      <RaisedButton label="Crear Cuenta" secondary={true}/>
                    </div>
                  );
                }}></Route>
              <RaisedButton linkbutton containerElement={<Link to="/" />} label="Inicio" primary={true}/>
              </div>

          </div>
        </div>
        <div className="col-xs-12 col-sm-6">


            <div className="">
              <Route path="/login" exact render={() => <div className="login-background" style={{
                'backgroundImage': "url(" + process.env.PUBLIC_URL + '/images/flowers-roses-close-up.jpg' + ")"
              }}></div>}></Route>

              <Route path="/signup" exact render={() => <div className="login-background" style={{
                'backgroundImage': "url(" + process.env.PUBLIC_URL + '/images/pexels-photo-260954.jpeg' + ")"
              }}></div>}></Route>

            </div>

        </div>
      </div>

    );
  }
}
