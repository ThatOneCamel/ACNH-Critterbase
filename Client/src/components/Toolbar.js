import React from 'react'
import Navbar from 'react-bootstrap/Navbar'
import bellImage from '../images/bells_big.png'

function Toolbar(){
    return(
        <Navbar bg="light" expand="lg">
            <Navbar.Brand>
                <img src={bellImage} width="30" height="30" alt="Bells Icon" />
            </Navbar.Brand>
        </Navbar>
    )
}

export default Toolbar;