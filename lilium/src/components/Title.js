import React from 'react';

import {purpleA700} from 'material-ui/styles/colors';


export default class Title extends React.Component {



  render(){
    return(

      <div  className="title-found" style={{'backgroundColor': purpleA700}}>
          <div>
            <img className="Header-Titulo" src={process.env.PUBLIC_URL + '/images/LILIUM-01.png'} />
          </div>
      </div>
    );
  }
}
