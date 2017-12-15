import React from 'react';

import { Card, CardText, CardMedia, CardTitle } from 'material-ui/Card';

import {tealA400,greenA400, yellow800} from 'material-ui/styles/colors';


export default class Benefits extends React.Component{
  render(){
    return(
      <section>
      <ul>
        <Card className="Header-Benefit">

          <CardText >

            <div className="row">
              <div className="Header-Benefit-image" style={{'backgroundColor': yellow800}}>
                <img src={process.env.PUBLIC_URL + '/images/ahorro-01.png'} />
              </div>
              <div className="Header-Benefit-content">
                <h3>Lo mejor para tu bolsillo</h3>
                <p>Encuentra los precios mas comodos de tu destino de envio</p>
              </div>
            </div>

          </CardText>
        </Card>
        <Card className="Header-Benefit">

          <CardText >
            <div className="row">
              <div className="Header-Benefit-image" style={{'backgroundColor': greenA400}}>
                <img src={process.env.PUBLIC_URL + '/images/mexico-01.png'} style={{'height':"80px"}}/>
              </div>
              <div className="Header-Benefit-content">
                <h3>Apoyas la economia local</h3>
                <p>Compra en los negocios locales como si estuvieras ahi</p>
              </div>
            </div>

          </CardText>
        </Card>
        <Card className="Header-Benefit">

          <CardText >
            <div className="row">
              <div className="Header-Benefit-image" style={{'backgroundColor':tealA400}}>
                <img src={process.env.PUBLIC_URL + '/images/ubicacion-01.png'} style={{'height':"120px"}}/>
              </div>
              <div className="Header-Benefit-content">
                <h3>Estamos en todo mexico</h3>
                <p>Somos la plataforma de las florerias locales mas grande del pais</p>
              </div>
            </div>

          </CardText>
        </Card>

      </ul>
        </section>
    );
  }
}
