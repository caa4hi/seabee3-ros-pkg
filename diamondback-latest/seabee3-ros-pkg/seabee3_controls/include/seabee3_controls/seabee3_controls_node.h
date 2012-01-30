/***************************************************************************
 *  include/seabee3_controls/seabee3_controls_node.h
 *  --------------------
 *
 *  Copyright (c) 2011, Edward T. Kaszubski ( ekaszubski@gmail.com )
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions are
 *  met:
 *
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above
 *    copyright notice, this list of conditions and the following disclaimer
 *    in the documentation and/or other materials provided with the
 *    distribution.
 *  * Neither the name of seabee3-ros-pkg nor the names of its
 *    contributors may be used to endorse or promote products derived from
 *    this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 *  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 *  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 *  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 *  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 *  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 *  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 *  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 **************************************************************************/

#ifndef SEABEE3CONTROLS_SEABEE3CONTROLSNODE_H_
#define SEABEE3CONTROLS_SEABEE3CONTROLSNODE_H_

#include <quickdev/node.h>
#include <quickdev/robot_controller_policy.h>
#include <quickdev/controllers/reconfigurable_pid.h>
#include <seabee3_driver/MotorVals.h>

typedef seabee3_driver::MotorVals _MotorValsMsg;
typedef quickdev::RobotControllerPolicy<_MotorValsMsg> _RobotController;

QUICKDEV_DECLARE_NODE( Seabee3Controls, _RobotController )

QUICKDEV_DECLARE_NODE_CLASS( Seabee3Controls )
{
    typedef quickdev::ReconfigurablePID<6> _Pid6D;

    _Pid6D pid_;

    QUICKDEV_DECLARE_NODE_CONSTRUCTOR( Seabee3Controls )
    {
        //
    }

    QUICKDEV_SPIN_FIRST()
    {
        initPolicies<_RobotController>( "robot_name_param", std::string( "seabee3" ) );

        pid_.applySettings(
            quickdev::make_shared( new _Pid6D::_Settings( "linear/x" ) ),
            quickdev::make_shared( new _Pid6D::_Settings( "linear/y" ) ),
            quickdev::make_shared( new _Pid6D::_Settings( "linear/z" ) ),
            quickdev::make_shared( new _Pid6D::_Settings( "angular/x" ) ),
            quickdev::make_shared( new _Pid6D::_Settings( "angular/y" ) ),
            quickdev::make_shared( new _Pid6D::_Settings( "angular/z" ) )
        );

        initPolicies<quickdev::policy::ALL>();
    }

    QUICKDEV_SPIN_ONCE()
    {
        pid_.update<0>( 0, 0 );
        _RobotController::update( _MotorValsMsg() );
    }
};

#endif // SEABEE3CONTROLS_SEABEE3CONTROLSNODE_H_
