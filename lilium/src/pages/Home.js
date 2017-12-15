import React from 'react';

import {purpleA700} from 'material-ui/styles/colors';

import Title from '../components/Title';
import Benefits from '../components/Benefits.js';
import PlaceCard from '../components/places/PlaceCard';
import RaisedButton from 'material-ui/RaisedButton';
import Footer from '../components/footer'

import MyAppBar from '../components/navigation/MyAppBar';

import {BrowserRouter as ReactRouter, Link, Route} from 'react-router-dom';

import TransitionGroup from 'react-transition-group/TransitionGroup';

export default class Home extends React.Component {



  render() {
    return (
      <section>
        <div className="Header-background">
          <div style={{"margin": "0 auto"}}>
            <div className="Header-main">
            <div className="Botones-Inicio">
              <div>

              <RaisedButton linkbutton containerElement={<Link to="/signup" />} label="Crear cuenta gratuita" secondary={true}/>

              </div>
              <div>
                  <RaisedButton linkbutton containerElement={<Link to="/login" />} label="Iniciar Secion" secondary={true}/>
              </div>
            </div>
              <Title></Title>

            </div>
            <div>
              <Benefits/>
            </div>
            <div>
              <MyAppBar/>
            </div>
            <div>
              <Footer></Footer>
            </div>
          </div>

        </div>
      </section>
    );
  }

}
