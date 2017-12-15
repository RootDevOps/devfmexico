import React from 'react';


export default class Footer extends React.Component {
  render() {
    return (

      <div className="footer" style={{'backgroundColor': "#58606d"}}>
        <div className="footer-left">
          <div className="horizontal-footer">
            <div><img className="iconos-footer" src={process.env.PUBLIC_URL + '/images/ubicacion.png'}/></div>
            <div><h2>Impac Hub s/n</h2></div>
          </div>
          <div className="horizontal-footer">
            <div><img className="iconos-footer" src={process.env.PUBLIC_URL + '/images/icono-telefono.png'}/></div>
            <div><h2>762106685612</h2></div>
          </div>
          <div className="horizontal-footer">
            <div><img className="iconos-footer" src={process.env.PUBLIC_URL + '/images/email_icon_relleno.png'}/></div>
            <div><h3>Lilium_Mexico@gmail.com</h3></div>
          </div>

        </div>

        <div className="footer-rigth">
          <div >
              <div>  <img  src={process.env.PUBLIC_URL + '/images/LILIUM-01.png'}  style={{'width':"150px"}}/></div>
              <div><h2>Conectando con lo tradicinal</h2></div>
          </div>
          <div>
            <div></div>
            <div><p>Somos una empresa comprometida a traer <br/> venta externa a negocios locales</p></div>
          </div>
          <div className="redes-sociales">
              <div>
                <div><img className="iconos-footer" src={process.env.PUBLIC_URL + '/images/facebook_icon_relleno.png'}/></div>
              </div>
              <div>
                <div><img className="iconos-footer" src={process.env.PUBLIC_URL + '/images/ICONO-INSTAGRAM.png'}/></div>
              </div>
              <div>
                <div><img className="iconos-footer" src={process.env.PUBLIC_URL + '/images/icono-twitter.png'}/></div>
              </div>
          </div>

        </div>
      </div>
    );
  }

}
