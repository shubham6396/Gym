import { Table, Button, List, Avatar, Typography, Tag, Divider, Form, Descriptions } from 'antd';
import { EditOutlined, MessageOutlined, LikeOutlined, StarOutlined } from '@ant-design/icons';
import {Link, withRouter} from "react-router-dom";
import React from "react";
import axios from 'axios'
import { Card } from 'antd';
import swal from "sweetalert";
import * as actionTypes from "../User/store/Actions/ActionTypes";


const gridStyle = {
  width: '25%',
  textAlign: 'center',
};

// reservation
const { Column } = Table;

const descriptionStyles = {
    marginLeft: '1%',
    padding: 10,

};

class UserProfile extends React.Component {

    state = {
        userData: {},
        reservationData: [],
        cancelledReservationId: null,
        WLData: []
    };

    componentDidMount() {
        console.log("Profile Component Mounted")
        const usrId = localStorage.getItem('token');
        console.log(usrId);
        axios.get("http://127.0.0.1:8000/user/getUserInfo?usrId=" + usrId).then(res => {


            this.setState({
                userData: res.data.Data
            })


        }).catch(error => console.log(error));

        axios.get("http://127.0.0.1:8000/reservation/getReservationsForUser?usrId=" + usrId).then(res => {

            console.log(res.data.Reservations)
            this.setState({
                reservationData: res.data.Reservations
            })
            console.log(this.state)

        }).catch(error => console.log(error));



    }

    cancelReservation = record => {

        const reservationId = record.reservationId;
        const usrId = this.state.userData.usrId;

        swal({
          title: "Are you sure you want to Cancel this Reservation?",
          icon: "warning",
          dangerMode: true,
          buttons: [ "No, I'm not Sure", "Yes, Cancel it"]
        })
        .then((willDelete) => {
          if (willDelete) {
              swal("Your Reservation at "+record.startTime+" has been Cancelled", {
              icon: "success",
            }).then(value => {

                axios.get("http://127.0.0.1:8000/reservation/cancelReservation?reservationId=" + reservationId).then(res1=> {

                    axios.get("http://127.0.0.1:8000/reservation/getReservationsForUser?usrId=" + usrId).then(res2 => {

                        console.log(res2.data.Reservations);
                        this.setState({
                            reservationData: res2.data.Reservations,
                            cancelledReservationId: res1.data.reservationId
                        });
                        console.log(this.state)

                    }).catch(error => console.log(error));
                    console.log(this.state);

                }).catch(err=> console.log(err))

              });


          } else {
            swal("Your Reservation at "+record.startTime+ " is Intact");
            console.log(window.location.pathname);
          }

        });

    };


    render() {
        let myNotes;

        if (localStorage.getItem('is_WL') == 1) {
            myNotes = <span>Your WaitList is now available, please check the table on the button of this page to add it to Reservation or Cancel it!</span>;
        } else {
            myNotes = <span>Your WaitList is now unavailable</span>;
        }

        return (
            <div className="site-card-border-less-wrapper">
                <h4><b>Notifications: </b>{myNotes}</h4>

                <Card title="User Information" bordered={true} style={{ width: 1000, marginBottom: '50px' }}>
                  <Descriptions style = {descriptionStyles} >
                      <Descriptions.Item label="First Name">{this.state.userData.usrFirstName}</Descriptions.Item>
                      <Descriptions.Item label="Last Name">{this.state.userData.usrLastName}</Descriptions.Item>
                      <Descriptions.Item label="Student ID">{this.state.userData.usrId}</Descriptions.Item>
                      <Descriptions.Item label="Username">{this.state.userData.usrLoginName}</Descriptions.Item>
                      <Descriptions.Item label="Email ID">{this.state.userData.usrEmailId}</Descriptions.Item>
                      <Descriptions.Item label="Phone Number">{this.state.userData.usrContact}</Descriptions.Item>
                  </Descriptions>
                </Card>
                
                {/* click <Link to="/register/"><EditOutlined/></Link> to make changes. */}
                <hr/>
                <h4 style = {descriptionStyles}><b>My Reservations</b></h4>
                <Table dataSource={this.state.reservationData}>
                  <Column title="Sport" dataIndex="sportName" key="sportName" />
                  <Column title="Area Name" dataIndex="areaName" key="areaName" />
                  <Column title="Equipment" dataIndex="equipmentName" key="equipmentName" />
                  <Column title="Date" dataIndex="reservationDate" key="reservationDate" />
                  <Column title="Start Time" dataIndex="startTime" key="startTime" />
                  <Column title="End Time" dataIndex="endTime" key="endTime" />
                  <Column
                    title="Action"
                    key="action"
                    render={(text, record) => (
                      <span>
                        <Button type = "primary" style={{ marginRight: 4}} onClick={() => this.cancelReservation.bind(this)(record)}>Cancel Reservation</Button>
                      </span>
                    )}
                  />
                </Table>

            </div>
        )
    }
}

export default UserProfile;

