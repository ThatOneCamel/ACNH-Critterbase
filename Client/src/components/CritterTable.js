import React from 'react'
import Table from 'react-bootstrap/Table'
import Image from 'react-bootstrap/Image'
import Container from 'react-bootstrap/Container'
import insectImg from '../images/bugs/01_Common.png'
//import fishImg from '../images/fish/tile336.png'
import bellSmall from '../images/bells_small.png'

function CritterTable(){
    return(
        <Container fluid>
        <Table striped bordered hover responsive fluid>
            <thead>
                <tr>
                <th>#</th>
                <th>Image</th>
                <th>Name</th>
                <th>Location</th>
                <th>NorthernHemi</th>
                <th>SouthernHemi</th>
                <th>Time</th>
                <th>Shadow Size</th>
                <th>Bells</th>
                </tr>
            </thead>

            <tbody>
                <tr>
                <td>1</td>
                <td> <Image src={insectImg} width="70" height="70"></Image></td>
                <td>Common Butterfly</td>
                <td>Flying</td>
                <td>September-June</td>
                <td>March-December</td>
                <td>4AM - 7PM</td>
                <td>N/A</td>
                <td><Image src={bellSmall} width="35" height="35" fluid></Image> 7000 </td>
                </tr>
                <tr>
                <td>2</td>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
                </tr>
                <tr>
                <td>3</td>
                <td colSpan="2">Larry the Bird</td>
                <td>@twitter</td>
                </tr>
            </tbody>
        </Table>
        </Container>
    )
}

export default CritterTable;