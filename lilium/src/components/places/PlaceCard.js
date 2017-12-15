import React from 'react';

import { Card, CardText, CardMedia, CardTitle, CardActions } from 'material-ui/Card';

import FlatButton from 'material-ui/FlatButton';

import {indigo400,redA400,lightBlueA400,amberA400,purpleA700} from 'material-ui/styles/colors';

import FadeAndScale from '../animations/FadeAndScale';


export default class PlaceCard extends React.Component{
  constructor(props){
      super(props);
      this.state = {
        show: true
      }
  }


  render(){
    return(
      <FadeAndScale className="cards"  in={this.props.in}>
        <div className="cards-populares">
          <Card>
            <CardMedia className="CardMedia">
              <img src={this.props.imagen} style={{height:"300px"}}/>
            </CardMedia>
            <CardTitle title={this.props.nombre}></CardTitle>
            <CardText>{this.props.description}</CardText>

            <CardActions style={{'textAlign': 'right'}}>
              <FlatButton secondary={true} label="Ver más" />
              <FlatButton secondary={true} onClick={this.props.ocultar} label="Ocultar" />
            </CardActions>
          </Card>
        </div>
      </FadeAndScale>
    );
  }
}
