PROGRAM PLC_Drain_System
  VAR
    X_Sensor_ON AT %IX0.1 : BOOL;
  END_VAR
  VAR
    C_Timer : BOOL;
    C_Buzer : BOOL;
  END_VAR
  VAR
    Y_Buzer AT %QX0.1 : BOOL;
    Y_Motor AT %QX0.2 : BOOL;
  END_VAR
  VAR
    Delay : TIME := T#1S;
    TP0 : TP;
    TON0 : TON;
  END_VAR

  Y_Motor := X_Sensor_ON;
  TP0(IN := NOT(C_Timer), PT := Delay);
  Y_Buzer := X_Sensor_ON AND TP0.Q;
  C_Buzer := NOT(TP0.Q);
  TON0(IN := C_Buzer AND NOT(C_Timer), PT := Delay);
  C_Timer := TON0.Q;
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : PLC_Drain_System;
  END_RESOURCE
END_CONFIGURATION
